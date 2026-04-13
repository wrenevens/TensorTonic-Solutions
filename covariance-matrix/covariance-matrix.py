import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.ndim < 2 or X.shape[0] < 2:
        return None
    X_cen = X - np.mean(X, axis=0)
    print(X.shape)
    return float(1.0/(X.shape[0]-1)) * (X_cen.T @ X_cen)

    