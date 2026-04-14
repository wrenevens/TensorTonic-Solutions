import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x)
    max_vals = None
    if x.ndim == 2:
        max_vals = np.max(x, axis=1, keepdims=True)
        exp = np.exp(x - max_vals)
        return exp / np.sum(exp, axis=1, keepdims=True)
    else:
        max_vals = np.max(x)
        exp = np.exp(x - max_vals)
        return exp / np.sum(exp)