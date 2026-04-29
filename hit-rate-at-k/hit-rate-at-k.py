def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    U = len(ground_truth)

    c = 0
    for id, items in enumerate(ground_truth):
        win = recommendations[id][:k]
        for item in items:
            if item in win:
                 c += 1
    return (1 / U) * c
        
    