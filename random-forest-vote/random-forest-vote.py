import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions = np.array(predictions)
    N, D = predictions.shape
    L = np.max(predictions) + 1

    offset = np.arange(D) * L
    shifted = predictions + offset

    counts = np.bincount(shifted.ravel()).reshape((D, L))

    return np.argmax(counts, axis=1).tolist()