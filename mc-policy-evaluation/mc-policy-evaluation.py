import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    result = {}
    rv = [[] for _ in range(n_states)]

    for ep in episodes:
        g=0
        i=0
        vst=set()
        for s, r in ep[::-1]:
            g =gamma* g + r
            if s not in vst:
                rv[s].append(g)
            else:
                rv[s]=g
            vst.add(s)
            i+=1
    V = np.array([np.mean(r) if r else 0.0 for r in rv])
    return V
