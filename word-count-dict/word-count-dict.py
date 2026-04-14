def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    result = {}
    for sen in sentences:
        for tok in sen:
            if tok not in result:
                result[tok] = 1
            else:
                result[tok] += 1
    return result