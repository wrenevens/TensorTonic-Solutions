def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    filtered_score = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    
    filtered_score.sort(key=lambda x: -x[0])
    
    top_k = filtered_score[:k]
    result = []
    for score in top_k:
        result.append(score[1])
    return result
    

    

    
    