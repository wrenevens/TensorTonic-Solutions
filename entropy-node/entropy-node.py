import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y, dtype=float)
    values, counts = np.unique(y, return_counts=True)
    probs = counts / np.sum(counts)
    return -(np.sum(probs * np.log2(probs)))