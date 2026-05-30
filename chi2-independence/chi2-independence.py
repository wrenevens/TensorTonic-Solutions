import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C)

    rows = np.sum(C, axis=0, keepdims=True)
    cols = np.sum(C, axis=1, keepdims=True)
    total = np.sum(C)
    E = (rows * cols) / total

    return np.sum((C - E)**2 / E), E