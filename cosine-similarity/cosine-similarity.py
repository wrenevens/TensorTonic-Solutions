import numpy as np
from numpy.linalg import norm
def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if (a == 0).all() or (b == 0).all():
        return 0.0
    
    return np.dot(a, b) / (
        norm(a) * norm(b)
    )