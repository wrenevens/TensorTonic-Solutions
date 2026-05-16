import numpy as np
import math

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    positions = np.arange(seq_len)[:, np.newaxis]
    dims = np.arange(d_model)[np.newaxis, :]

    exponent = 2 * (dims//2) / d_model
    angles = positions / (base**exponent)

    PE = np.empty_like(angles)
    PE[:, 0::2] = np.sin(angles[:, 0::2])
    PE[:, 1::2] = np.cos(angles[:, 1::2])
    return PE