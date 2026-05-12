import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    y = np.array(y)
    d = np.linalg.norm(a - b, axis=1) if a.ndim >= 2 else np.linalg.norm(a - b)
    loss = y*d**2 + (1-y)*np.maximum(0, margin - d)**2
    return np.sum(loss) if reduction=="sum" else np.mean(loss)