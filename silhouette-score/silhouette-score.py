import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    labels = np.asarray(labels)
    unique, inv = np.unique(labels, return_inverse=True)
    K = len(unique)
    N = len(labels)

    if K <= 1 or K == N:
        return 0.0

    sq = (X**2).sum(axis=1)
    dist = np.sqrt(np.clip(sq[:, None] + sq[None, :] - 2 * (X @ X.T), 0, None))

    membership = (inv[:, None] == np.arange(K)[None, :]).astype(float)
    cluster_sizes = membership.sum(axis=0)

    sum_dist = dist @ membership

    same_cluster_size = cluster_sizes[inv] - 1
    intra = sum_dist[np.arange(N), inv] / np.maximum(same_cluster_size, 1)

    avg_dist = sum_dist / np.maximum(cluster_sizes, 1)
    avg_dist[membership.astype(bool)] = np.inf
    inter = avg_dist.min(axis=1)

    max_val = np.maximum(inter, intra)

    s = np.where(max_val > 0, (inter - intra) / max_val, 0.0)

    s[same_cluster_size == 0] = 0.0

    return float(np.mean(s))
    