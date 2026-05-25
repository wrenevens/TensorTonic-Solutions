def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here
    result = {
        "counts" : {},
        "probs"  : {}
    }

    vocab = set(tokens)

    for i in range(len(tokens) - 1):
        bigram = tuple(tokens[i:i+2])
        result["counts"][bigram] = result["counts"].get(bigram, 0 ) + 1

    counts = {}
    for w1, w2 in result["counts"]:
        counts[w1] = counts.get(w1, 0) + result["counts"][(w1, w2)]
    
    for w1 in vocab:
        denominator = counts.get(w1, 0) + len(vocab)
        for v in vocab:
            numerator = result["counts"].get((w1, v), 0) + 1
            result["probs"][(w1, v)] = numerator / denominator
        
    
    return result["counts"], result["probs"]