import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    rv = []
    g=0
    for s, r in list(zip(states, rewards))[::-1]:
        g = g *gamma + r
        rv.append(g)
    rv.reverse()
    rv = np.array(rv)
    V = np.array(V)
    return rv - V
    
        
