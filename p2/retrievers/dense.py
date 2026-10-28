"""Dense retrieval: embed every chunk once, embed the query, rank chunks by cosine similarity.

The embedder is bge-small-en-v1.5 (the 12 lab's "bge" arm: no query instruction prefix) unless p2.toml
has a [dense] table with a `model` line. Chunk vectors are cached in .cache/vectors/, so only the
first run encodes the corpus. Every vector has length 1, so one matrix product gives all the cosines,
and a document scores its best chunk (ChunkScorer does that lift).
"""

from __future__ import annotations

import numpy as np

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.model = cfg.table("dense").get("model", embed.BGE)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> np.ndarray:
        query = self.embedder.encode([text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
