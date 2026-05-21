import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    accuracy = float(np.sum(y_true == y_pred) / len(y_true))

    classes = np.unique(np.concatenate([y_true, y_pred]))
    n_classes = len(classes)
    confusion_matrix = np.zeros((n_classes, n_classes), dtype=int)
    for i, cls_true in enumerate(classes):
        for j, cls_pred in enumerate(classes):
            confusion_matrix[i, j] = np.sum((y_true == cls_true) & (y_pred == cls_pred))

    tp = np.diagonal(confusion_matrix)
    fp = np.sum(confusion_matrix, axis=0) - tp
    fn = np.sum(confusion_matrix, axis=1) - tp

    support = np.sum(confusion_matrix, axis=1).astype(float)

    safe_div = lambda num, denom: np.divide(num, denom, out=np.zeros_like(num, dtype=float), where=denom != 0)

    match average:
        case "binary":
            if pos_label not in classes:
                precision, recall, f1 = 0.0, 0.0, 0.0
            else:
                idx = np.where(classes == pos_label)[0][0]
                precision = float(safe_div(tp[idx], tp[idx] + fp[idx]))
                recall = float(safe_div(tp[idx], tp[idx] + fn[idx]))
                f1 = float(safe_div(2 * precision * recall, precision + recall))

        case "micro":
            global_tp = np.sum(tp)
            global_fp = np.sum(fp)
            global_fn = np.sum(fn)
            
            precision = float(safe_div(global_tp, global_tp + global_fp))
            recall = float(safe_div(global_tp, global_tp + global_fn))
            f1 = float(safe_div(2 * precision * recall, precision + recall))

        case "macro":
            class_precision = safe_div(tp, tp + fp)
            class_recall = safe_div(tp, tp + fn)
            class_f1 = safe_div(2 * class_precision * class_recall, class_precision + class_recall)
            
            precision = float(np.mean(class_precision))
            recall = float(np.mean(class_recall))
            f1 = float(np.mean(class_f1))

        case "weighted":
            class_precision = safe_div(tp, tp + fp)
            class_recall = safe_div(tp, tp + fn)
            class_f1 = safe_div(2 * class_precision * class_recall, class_precision + class_recall)
            
            total_support = np.sum(support)
            if total_support == 0:
                precision, recall, f1 = 0.0, 0.0, 0.0
            else:
                precision = float(np.sum(class_precision * support) / total_support)
                recall = float(np.sum(class_recall * support) / total_support)
                f1 = float(np.sum(class_f1 * support) / total_support)
                
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }