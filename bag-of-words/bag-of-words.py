import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    lookup = {}
    for w in vocab:
        lookup[w] = 0
        
    for t in tokens:
        if lookup.get(t) is None:
            continue
        else:
            lookup[t] += 1
    result = [c for c in lookup.values()]
    return np.asarray(result, dtype=int)
    