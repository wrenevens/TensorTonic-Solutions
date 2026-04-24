def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for d in range(order):
        series = [series[i] - series[i-1] for i in range(1, len(series))]
    return series
            