def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    result = []
    for t in range(len(returns)):
        w_t = 1.0
        for i in range(t + 1):
            w_t *= (1.0 + returns[i])
        result.append(w_t - 1.0)
    return result
        
            
        