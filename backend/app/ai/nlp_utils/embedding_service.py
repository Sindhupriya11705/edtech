from sentence_transformers import SentenceTransformer
import numpy as np

_model: SentenceTransformer | None = None

def get_embedding_model() -> SentenceTransformer:
    global _model
    if _model is None:
        # Using a compact, performant model
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def embed_text(text: str) -> np.ndarray:
    """
    Returns a 1D numpy array embedding for the given text.
    """
    model = get_embedding_model()
    return model.encode(text, normalize_embeddings=True)