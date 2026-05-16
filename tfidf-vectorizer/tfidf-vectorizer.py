import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Initialize vocabulary
    vocabulary = set()
    
    def count_terms(doc: str):
        # Count tokens, and build vocab
        tokens = doc.lower().split()
        for tok in tokens:
            vocabulary.add(tok)
        return len(tokens)

    # If documents is empty
    if not documents:
        return np.empty((0, 0)), []

    count = [Counter(doc.lower().split()) for doc in documents]
    total_terms_in_d = [count_terms(doc) for doc in documents]
    vocabulary = sorted(vocabulary)
    term2idx = {term : i for i, term in enumerate(vocabulary)}

    # calc term frequency
    # tf has shape=n_docs, n_vocab
    # because output requires shape(n_docs, n_vocab)
    tf_t_d = np.zeros((len(documents), len(vocabulary)))
    for d in range(len(documents)):
        for t in vocabulary:
            tf_t_d[d, term2idx[t]] = count[d][t] / total_terms_in_d[d]

    # calc idf
    df = np.sum(tf_t_d > 0, axis=0)
    idf_t = np.log(len(documents) / df)
    

    return tf_t_d * idf_t, vocabulary
        
    

    

    
    

    