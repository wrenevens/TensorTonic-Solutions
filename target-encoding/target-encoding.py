def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    lookup = {}
    for i in range(len(targets)):
        if lookup.get(categories[i]) is None:
            lookup[categories[i]] = [targets[i], 1]
        else:
            lookup[categories[i]][0] += targets[i]
            lookup[categories[i]][1] += 1
    return [lookup[key][0] / lookup[key][1] for key in categories]