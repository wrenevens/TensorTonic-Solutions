import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    e = y_true - y_pred
    return np.mean(np.piecewise(
        e,
        [np.abs(e) <= delta, np.abs(e) > delta],
        [lambda x: 1/2 * (x**2), 
         lambda x: delta * (np.abs(x)) - 1/2 * (delta**2)
        ]
    ))


