def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    for i in range(1, len(values)):
        values[i] = alpha * values[i] + (1 - alpha) * values[i - 1]
    return values