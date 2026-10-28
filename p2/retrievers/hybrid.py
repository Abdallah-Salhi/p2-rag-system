"""Hybrid retrieval: reciprocal rank fusion (RRF) of bm25 and dense.

Each item scores the sum of 1 / (60 + rank) over the two rankings, ranks starting at 1, so an item
near the top of both lists beats one that is first in only one. This is the 13 lab's rrf() with k = 60.

Both systems are asked for their full rankings, not top-10 lists, because a document that is 11th in
both lists can belong in the fused top 10. Documents fuse for `search`; chunks fuse the same way for
`search_chunks`, which `p2 answer` needs.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False

RRF_K = 60
PARTS = ("bm25", "dense")


def fuse(rankings):
    """RRF over rankings, each a best-first list of (id, score); returns (id, fused score) best first."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, (item, _) in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1.0 / (RRF_K + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.parts = [retrievers.build(name, corpus, cfg) for name in PARTS]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(self.parts[0].chunks)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        return fuse(part.search(text, self.n_docs) for part in self.parts)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        return fuse(part.search_chunks(text, self.n_chunks) for part in self.parts)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
