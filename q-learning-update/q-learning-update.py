import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.array(Q, dtype=float)
    Q_new = Q.copy()
    td_error = (r + gamma * np.max(Q[s_next, :]) - Q[s][a])
    Q_new[s][a] = Q[s][a] + alpha * td_error
    return Q_new