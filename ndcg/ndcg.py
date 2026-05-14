import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    k = min(len(relevance_scores), k)
    dcg = sum([(2**relevance_scores[i]-1)/(math.log2(i+2)) for i in range(k)])
    sorted_rel = sorted(relevance_scores, reverse=True)
    idcg = sum([(2**sorted_rel[i]-1)/(math.log2(i+2)) for i in range(k)])

    if idcg==0.0:
        return 0.0
    return dcg/idcg
    