import numpy as np

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    K = len(predictions)
    q = []
    for i in range(K):
        if i == target:
            q.append(1 - epsilon + epsilon/K)
        else:
            q.append(epsilon/K)
    q = np.array(q)
    predictions = np.array(predictions)
    return - np.sum(q * np.log(predictions))
        