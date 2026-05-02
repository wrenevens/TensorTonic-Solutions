import numpy as np
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    values = np.array(values)
    delta = 2.0 * np.pi * values / period
    return np.column_stack((np.sin(delta), np.cos(delta))).tolist()