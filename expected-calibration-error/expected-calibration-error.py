def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    bins = [[] for _ in range(n_bins)]
    
    for i in range(len(y_true)):
        bin_idx = int(y_pred[i] * n_bins)
        if bin_idx == n_bins:
            bin_idx -= 1
        bins[bin_idx].append(i)
    
    ece = 0.0
    n_samples = len(y_pred)
    
    for bin_indices in bins:
        n_bin = len(bin_indices)
        if n_bin == 0:
            continue
            
        sum_conf = 0.0
        sum_acc = 0.0
        for idx in bin_indices:
            sum_conf += y_pred[idx]
            sum_acc += y_true[idx]
        
        avg_conf = sum_conf / n_bin
        avg_acc = sum_acc / n_bin
        
        ece += abs(avg_conf - avg_acc) * (n_bin / n_samples)
        
    return ece
    
            
            
        