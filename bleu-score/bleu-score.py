import math
def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    # Write code here
    p_n = 0.0
    for n in range(1, max_n + 1):
        candidate_counts = {}
        reference_counts = {}
        
        for i in range(0, len(candidate) - n + 1):
            word = " ".join(candidate[i:i+n])
            candidate_counts[word] = candidate_counts.get(word, 0) + 1

        for i in range(0, len(reference) - n + 1):
            word = " ".join(reference[i:i+n])
            reference_counts[word] = reference_counts.get(word, 0) + 1

        candidate_total_count = len(candidate) - n + 1
        clipped_matches = 0
        for word, cnt in candidate_counts.items():
            clipped_matches += min(cnt, reference_counts.get(word, 0))
        if clipped_matches == 0:
            return 0.0

        print(f"{n} gram : {math.log(clipped_matches / candidate_total_count)} ")
        p_n += math.log(clipped_matches / candidate_total_count)
        print(f"p_n: {p_n}")

    r = len(reference)
    c = len(candidate)
    BP = 1.0 if c >= r else math.exp(1 - r/c)
    return BP * math.exp(p_n / max_n)