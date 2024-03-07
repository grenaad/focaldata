from domain.contracts import Embedding
from llama_index.core.base.embeddings.base import similarity, SimilarityMode

def similarity_score (embedding1: Embedding, embedding2: Embedding) -> float:
    score_val: float = 0.0
    try:
        # SimilarityMode.DEFAULT = "cosine"
        score_val = similarity(embedding1, embedding2, SimilarityMode.DEFAULT )
    except Exception:
        pass
    return score_val

