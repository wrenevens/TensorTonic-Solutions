def dot(x1, x2):
    return sum(a*b for a, b in zip(x1, x2))


def norm(x1):
    return math.sqrt(sum(a*a for a in x1))

    
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    cosine = dot(x1, x2) / (norm(x1) * norm(x2))

    if label == 1:
        return 1 - cosine
    return max(0, cosine - margin)