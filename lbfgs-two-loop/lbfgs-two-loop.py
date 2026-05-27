def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    # Write code here
    rho = [1.0 / _dot(s, y) for s, y in zip(s_list, y_list)]
    q = grad.copy()
    alpha = [0.0] * len(s_list)
    for i in range(len(s_list) - 1, -1, -1):
        alpha[i] = rho[i] * _dot(s_list[i], q)
        q = [q_k - alpha[i] * y_k for q_k, y_k in zip(q, y_list[i])]
    m = len(s_list)
    gamma = _dot(s_list[m - 1], y_list[m - 1]) / _dot(y_list[m - 1], y_list[m - 1])
    r = [gamma * q_k for q_k in q]
    for i in range(m):
        beta = rho[i] * _dot(y_list[i], r)
        r = [r_k + s_k * (alpha[i] - beta) for r_k, s_k in zip(r, s_list[i])]
    return [-x for x in r]

    
