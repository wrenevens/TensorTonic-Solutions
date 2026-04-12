import numpy as np
from scipy.special import comb

def _pmf(n, p, i):
    return comb(n, i) * pow(p, i) * pow(1-p, n-i)

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = _pmf(n, p, k)
    cdf = 0.0
    for i in range(k+1):
        cdf += _pmf(n, p, i)
    return float(pmf), float(cdf)