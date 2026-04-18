def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    result = []
    for score, votes in items:
        v_m = votes + min_votes
        wr = votes / v_m * score + min_votes / v_m * global_mean
        result.append(wr)
    return result