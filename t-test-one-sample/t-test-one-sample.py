import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    if n == 1:
        return 0
    sum = np.sum((x - np.mean(x)) ** 2)
    if sum == 0:
        return np.inf
    s = np.sqrt(sum / (n - 1))
    return (np.mean(x) - mu0) / (s / np.sqrt(n))