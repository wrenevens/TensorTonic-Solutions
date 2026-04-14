def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    result = []
    for p in points:
        best_dist = float('inf')
        best_idx = 0
        for idx, c in enumerate(centroids):
            dist_c = sum((p[d] - c[d])**2 for d in range(len(p)))
            if dist_c < best_dist:
                best_dist = dist_c
                best_idx = idx
        result.append(best_idx)
    return result
        