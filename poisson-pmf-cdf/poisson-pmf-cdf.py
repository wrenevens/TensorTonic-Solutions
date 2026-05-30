import numpy as np
import math 

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    indices = np.arange(k + 1)
    k_factorial = np.zeros(k + 1)
    k_factorial[1:] = np.cumsum(np.log(indices[1:]))

    p = np.exp(-lam + indices * np.log(lam) - k_factorial)
    return p[k], np.sum(p)
    
    