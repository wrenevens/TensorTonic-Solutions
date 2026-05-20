import numpy as np

def rnn_step_backward(dh, cache):
    """
    Returns:
        dx_t: gradient wrt input x_t      (shape: D,)
        dh_prev: gradient wrt previous h (shape: H,)
        dW: gradient wrt W               (shape: H x D)
        dU: gradient wrt U               (shape: H x H)
        db: gradient wrt bias            (shape: H,)
    """
    # Write code here
    dh = np.array(dh)
    x_t = np.array(cache[0], dtype=float)
    h_prev = np.array(cache[1], dtype=float)
    h_t = np.array(cache[2], dtype=float)
    W = np.array(cache[3], dtype=float)
    U = np.array(cache[4], dtype=float)
    b = np.array(cache[5], dtype=float)

    dz = dh * (1 - h_t**2)
    dW = np.outer(dz, x_t.T)
    dU = np.outer(dz, h_prev.T)
    db = dz
    dx_t = W.T @ dz
    dh_prev = U.T @ dz
    return dx_t, dh_prev, dW, dU, db
    
    
    