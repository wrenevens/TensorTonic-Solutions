import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.asarray(A, dtype=float)
    res = 0
    for i in range(A.shape[0]):
        res += A[i][i]
        
    return res
