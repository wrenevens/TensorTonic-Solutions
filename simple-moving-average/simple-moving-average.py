def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    result = []
    for i in range(len(values) - window_size + 1):
        win = values[i:i+window_size]
        avg = 0.0
        for win_v in win:
            avg += win_v
        avg /= window_size
        result.append(avg)
    return result