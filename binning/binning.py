import math
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    max_X = max(values)
    min_X = min(values)

    if (max_X == min_X):
        return [0] * len(values)
    w = (max_X - min_X) / num_bins
    return [min(num_bins-1, int((v-min_X)/w)) for v in values]
    