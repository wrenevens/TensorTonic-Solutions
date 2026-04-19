def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    result = []
    for i in range(len(values) - window_size + 1):
        win = values[i:i+window_size].copy()
        win.sort()
        median = 0.0
        if window_size % 2 == 0:
            median = (win[window_size // 2 - 1] + win[window_size // 2]) / 2
        else:
            median = win[window_size // 2]
        result.append(median)
    return result