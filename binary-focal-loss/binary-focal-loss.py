import numpy as np
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    predictions = np.array(predictions)
    targets = np.array(targets)
    
    pt = np.where(targets == 1, predictions, 1 - predictions)
    return (-alpha * (1 - pt)**gamma * np.log(pt)).mean().item()