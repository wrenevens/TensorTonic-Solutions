import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.array(Z1)
    Z2 = np.array(Z2)
    N = Z1.shape[0]
    S = (Z1 @ Z2.T) / temperature
    S_stable = S - np.max(S)
    
    loss = - 1/N * np.sum(np.log(np.exp(np.diag(S_stable)) / np.sum(np.exp(S_stable), axis=-1)))
    return loss