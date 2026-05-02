import numpy as np
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    values = np.array(values)
    u_val, inverse, counts = np.unique(values, return_counts=True, return_inverse=True)
    return [c / len(values) for c in counts[inverse]]