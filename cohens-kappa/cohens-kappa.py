import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)
    
    v1, c1 = np.unique(rater1, return_counts=True)
    v2, c2 = np.unique(rater2, return_counts=True)

    p1 = c1 / np.sum(c1)
    p2 = c2 / np.sum(c2)

    c0 = 0
    for i in range(len(rater1)):
        if rater1[i] == rater2[i]:
          c0 += 1

    p0 = c0 / len(rater1)

    pe = np.dot(p1, p2)

    if pe == 1:
        return 1

    return (p0 - pe) / (1 - pe)

    
    
        