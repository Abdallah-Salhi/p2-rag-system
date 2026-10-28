"""Reranker: ask Claude to reorder the top 20 of hybrid, one claude -p call per query.

For a query it takes hybrid's best 20 documents and shows Claude each one as its best-matching chunk,
numbered 1 to 20. The reply is forced into {"order": [20 numbers]} (each from 1 to 20) with a JSON schema.
A reply that is not each number once, or a failed call, keeps the first-stage order for that query.
Documents below the 20 keep hybrid's order underneath. A reranker can only reorder its candidates: a
relevant document outside hybrid's top 20 is never rescued.

`search_chunks` does the same over hybrid's best 20 chunks, for `p2 answer`.
"""

from __future__ import annotations

from p2 import claude, retrievers
from p2.runfile import order

NEEDS_CLAUDE = True

CANDIDATES = 20

PROMPT = """Below are {n} passages from a document collection, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n: int) -> dict:
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": n}, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        self.cfg = cfg
        self.model = cfg.model
        self.first = retrievers.build("hybrid", corpus, cfg)
        self.text_of = {c.id: c.text for c in self.first.parts[0].chunks}

    def _reorder(self, query: str, ids: list[str], texts: list[str]) -> list[str]:
        """ids in Claude's order; the first-stage order if the call fails or the reply is not each number once."""
        n = len(ids)
        if n < 2:
            return ids
        passages = "\n\n".join(f"[{i}] {t}" for i, t in enumerate(texts, 1))
        reply = claude.call(
            PROMPT.format(n=n, query=query, passages=passages), schema(n),
            model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg),
        )
        picked = (reply.output or {}).get("order") if reply.error is None else None
        if not isinstance(picked, list) or sorted(picked) != list(range(1, n + 1)):
            return ids
        return [ids[i - 1] for i in picked]

    @staticmethod
    def _scored(top: list[str], rest: list[tuple[str, float]]) -> list[tuple[str, float]]:
        """Reranked ids first with falling scores, then the rest below them in their own order."""
        total = len(top) + len(rest)
        out = [(item, float(total - i)) for i, item in enumerate(top)]
        out += [(item, float(total - len(top) - j)) for j, (item, _) in enumerate(rest)]
        return order(out)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search(text, max(k, CANDIDATES))
        head, rest = ranked[:CANDIDATES], ranked[CANDIDATES:]
        best_chunk = {}
        for chunk_id, _ in self.first.search_chunks(text, len(self.text_of)):
            best_chunk.setdefault(chunk_id.split("#")[0], chunk_id)
        ids = [docid for docid, _ in head]
        texts = [self.text_of[best_chunk[d]] for d in ids]
        return self._scored(self._reorder(text, ids, texts), rest)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search_chunks(text, max(k, CANDIDATES))
        head, rest = ranked[:CANDIDATES], ranked[CANDIDATES:]
        ids = [chunk_id for chunk_id, _ in head]
        return self._scored(self._reorder(text, ids, [self.text_of[i] for i in ids]), rest)[:k]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
