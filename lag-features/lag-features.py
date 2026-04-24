def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    result = []
    max_lag = max(lags)
    for t in range(max_lag, len(series)):
        row = [series[t - l] for l in lags]
        result.append(row)
    print(result)
    return result
    