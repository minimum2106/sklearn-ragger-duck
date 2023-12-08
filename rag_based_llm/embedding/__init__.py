"""The module :mod:`rag_based_llm.embedding` contains functions to embed
transformers allowing to embed text.
"""

from ._sentence_transformer import SentenceTransformer

__all__ = ["SentenceTransformer"]