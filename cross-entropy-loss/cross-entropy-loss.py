import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    if len(y_true) != len(y_pred):
        return None
    y_true, y_pred = np.array(y_true), np.array(y_pred)
        
    loss = y_pred[np.arange(len(y_pred)), y_true]
    return -np.mean(np.log(loss))