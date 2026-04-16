import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    m = np.asarray(m)
    v = np.asarray(v)
    grad = np.asarray(grad)
    
    m = np.dot(beta1, m) + np.dot((1 - beta1), grad)
    v = np.dot(beta2, v) + np.dot((1 - beta2), (grad**2))
    m_p = m / (1 - pow(beta1, t))
    v_p = v / (1 - pow(beta2, t))

    param = param - lr * m_p / (np.sqrt(v_p) + eps)
    return param, m, v