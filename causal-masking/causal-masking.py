import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    scores = np.array(scores)
    *_, h, w = scores.shape

    mask = np.triu(np.ones((h, w), dtype=bool), k=1)

    masked_values = np.copy(scores)
    masked_values[..., mask] = mask_value
    return masked_values