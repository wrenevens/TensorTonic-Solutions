import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v=np.atleast_2d(v)
    v_norm=np.maximum(np.sqrt(np.sum(v**2, axis=1)), 1e-12)
    res=(v.T/v_norm).T
    return res.squeeze() if res.shape[0]==1 else res