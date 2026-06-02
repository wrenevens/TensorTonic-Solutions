def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    N = len(values)
    result = []
    for s in range(N):
        max_V = -1
        for a in range(len(transitions[s])):
            Q = rewards[s][a] + gamma * sum([
                transitions[s][a][s_t] * values[s_t] for s_t in range(N)
            ])
            if max_V < Q:
                max_V = Q
        result.append(max_V)
    return result
            
        