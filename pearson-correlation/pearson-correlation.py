import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.array(X)
    mean = np.mean(X, axis=0, keepdims=True)
    cov_matrix = X - mean
    cov_matrix = (cov_matrix.T @ cov_matrix) / (X.shape[0] - 1)
    std = np.std(X, axis=0, ddof=1)
    std_devs = np.outer(std, std)
    return cov_matrix / std_devs
