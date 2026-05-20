import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X = np.array(X)
    mean = np.mean(X, axis=0, keepdims=True)
    centerX = X - mean

    cov_matrix = (centerX.T @ centerX) / (X.shape[0] - 1)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    top_k_eigenvalues = eigenvalues[-k:][::-1]
    top_k_eigenvectors = eigenvectors[:, -k:][:, ::-1]
    return centerX @ top_k_eigenvectors