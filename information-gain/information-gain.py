import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    left_side = y[split_mask==True]
    right_side = y[split_mask==False]
    
    left_entp = _entropy(left_side)
    right_entp = _entropy(right_side)

    n_l = len(left_side)
    n_r = len(right_side)

    return _entropy(y) - (n_l/(len(y)) * left_entp + n_r/len(y) * right_entp)
