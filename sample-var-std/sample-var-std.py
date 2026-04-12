import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    mean = np.mean(x)
    n = len(x)
    var = np.sum(((x - mean) ** 2) / (n - 1))
    return var, np.sqrt(var)