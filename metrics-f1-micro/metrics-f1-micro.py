def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = 0
    for i in range(len(y_pred)):
        tp += int(y_pred[i] == y_true[i])

    fn = len(y_true) - tp
    fp = len(y_true) - tp

    return (2 * tp) / (2 * tp + fp + fn)