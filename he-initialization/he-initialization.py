import math
import numpy as np

def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    W = np.array(W)
    L = math.sqrt(6 / fan_in)
    return (W * 2 * L - L).tolist()