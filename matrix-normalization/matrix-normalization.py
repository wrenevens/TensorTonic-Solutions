import numpy as np

def normalize(matrix, axis, norm_type):
    match norm_type:
        case "l2":
            return np.sqrt(np.sum(np.square(matrix), axis=axis, keepdims=True))
            
        case "l1":
            return np.sum(np.abs(matrix), axis=axis, keepdims=True)
            
        case "max":
            return np.max(np.abs(matrix), axis=axis, keepdims=True)
        case _:
            raise ValueError("No matching norm_type")

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        return None
    try:
        norm = normalize(matrix, axis, norm_type)
        norm = np.broadcast_to(norm, matrix.shape)
    except:
        return None
    return matrix / (norm + 1e-12)
    