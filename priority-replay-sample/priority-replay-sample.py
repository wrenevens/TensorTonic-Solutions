def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code here
    powered_piorities = [pow(p, alpha) for p in priorities]
    sum_powered = sum(powered_piorities)
    
    sampling_probs = [pw / sum_powered for pw in powered_piorities]

    N = len(priorities)
    samping_weights = [pow(N * prob, -beta) for prob in sampling_probs]

    max_weight = max(samping_weights)
    norm_weights = [w / max_weight for w in samping_weights]

    return [sampling_probs, norm_weights]
    
    