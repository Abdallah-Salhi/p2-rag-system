"""Ablation of dense: the same bge-small retriever with chunks of 150 words instead of 300 (overlap stays 50)."""

from __future__ import annotations

from p2.retrievers import dense

NEEDS_CLAUDE = False

BASE = "dense"
CHUNK_WORDS = 150


def build(corpus, cfg):
    return dense.Dense(corpus, cfg.replace(chunk_words=CHUNK_WORDS))
