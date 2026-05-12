import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.array(anchor)
    positive = np.array(positive)
    negative = np.array(negative)

    def d(x, y):
        return np.squeeze(np.linalg.norm(x - y, axis=-1)**2)

    
    return np.maximum(0, d(anchor, positive) - d(anchor, negative) + margin).mean().item()
    