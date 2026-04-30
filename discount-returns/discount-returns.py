def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    result = []
    g = 0.0
    rws = rewards[::-1]
    for r in rws:
        g = r + gamma * g
        result.append(g)
    result.reverse()
    return result