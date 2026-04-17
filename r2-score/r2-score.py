import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    vals = np.unique(y_true)
    if len(vals) == 1:
        if np.array_equal(y_pred, y_true):
            return 1.0
        else:
            return 0.0
    
    y_mean = np.mean(y_true)
    sse = np.sum(np.square(y_true - y_pred))
    sst = np.sum(np.square(y_true - y_mean))
    return 1 -  sse / sst 
    