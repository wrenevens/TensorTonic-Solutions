def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stopwords = set(stopwords)
    return [x for x in tokens if not x in stopwords]