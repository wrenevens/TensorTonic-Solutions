import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    counter = [Counter(doc) for doc in docs]
    doc_length = np.array([len(doc) for doc in docs])
    avg_doc_length = np.mean(doc_length)
    
    # calc idf
    df = np.zeros(shape=(1, len(query_tokens)))
    for tok_idx in range(len(query_tokens)):
        for doc_idx in range(len(docs)):
            df[0][tok_idx] += int(counter[doc_idx].get(query_tokens[tok_idx]) != None)

    idf = np.log(((len(docs) - df + 0.5) / (df + 0.5)) + 1)
    # calc tf
    tf = np.zeros(shape=(len(query_tokens), len(docs)))

    for tok_idx in range(len(query_tokens)):
        for doc_count_idx in range(len(counter)):
            tf[tok_idx][doc_count_idx] = counter[doc_count_idx][query_tokens[tok_idx]]
    # calc score
    score = (idf @ ((tf * (k1 + 1)) / (tf + k1*(1 - b + b * doc_length/avg_doc_length))))
    return score.squeeze(0)
        
        
        