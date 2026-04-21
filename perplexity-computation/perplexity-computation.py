import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    sum = 0.0
    for i in range(len(actual_tokens)):
        p = prob_distributions[i][actual_tokens[i]]
        sum += math.log(p)
    H = -1/len(actual_tokens) * sum
    return math.exp(H)