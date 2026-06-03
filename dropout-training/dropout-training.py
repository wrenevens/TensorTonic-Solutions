import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    if not rng:
        rng = np.random

    x = np.array(x)
    mask = (rng.random(x.shape) >= p) / (1.0 - p)
    output = x * mask
    
    return output, mask