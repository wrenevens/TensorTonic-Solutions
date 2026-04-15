import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    N, D = X.shape
    w = np.zeros(D)
    b = 0.0
    for i in range(steps):
        p = _sigmoid(X @ w + b)
        error = p - y

        grad_w = X.T @ error / len(y)
        grad_b = np.mean(error)

        w = w - np.dot(lr, grad_w)
        b = b - lr * grad_b
    return w, b