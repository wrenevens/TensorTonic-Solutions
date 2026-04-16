def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    relevant = set(relevant)
    top_k = recommended[:k]

    top_k_and_relevant_counts = 0
    for i in range(k):
        top_k_and_relevant_counts += int(top_k[i] in relevant)

    prec_k = top_k_and_relevant_counts / k
    recall_k = top_k_and_relevant_counts / len(relevant)

    return [prec_k, recall_k]