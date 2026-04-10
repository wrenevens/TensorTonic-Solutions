import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    B = []
    for col in range(len(A[0])):
        B.append([A[0][col]])

    for row in range(1, len(A)):
        for col in range(len(A[row])):
            B[col].append(A[row][col])
    return np.array(B)
