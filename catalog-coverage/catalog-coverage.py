def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    if n_items == 0:
        return 0.0
    items = set()
    for user in recommendations:
        for item in user:
            items.add(item)
    return len(items) / n_items
        