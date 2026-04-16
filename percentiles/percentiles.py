import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    return np.sort(np.percentile(x, q, method='linear'))