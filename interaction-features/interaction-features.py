def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    result = []
    for features in X:
        res_row = []
        for i in range(len(features)):
            for j in range(i + 1, len(features)):
                res_row.append(features[i] * features[j])
        result.append(features + res_row)
    return result
        