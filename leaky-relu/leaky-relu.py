import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    return np.piecewise(
        x,
        [x>=0, x<0],
        [lambda k: k, lambda k: alpha*k]
    )