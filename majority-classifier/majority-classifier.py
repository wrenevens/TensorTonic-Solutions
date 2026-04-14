import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    vals, counts = np.unique(y_train, return_counts=True)
    return [vals[np.argmax(counts)] for _ in X_test] 