def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    lkup = {}
    for i, s in enumerate(ordering):
        lkup[s] = i

    return [lkup[v] for v in values]