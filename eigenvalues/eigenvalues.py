import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    if not matrix or not isinstance(matrix, list):
        return None
    if not all(isinstance(row, list) and len(row) == len(matrix) for row in matrix):
        return None
    matrix = np.array(matrix)

    eigenvalues = np.linalg.eigvals(matrix)

    return eigenvalues