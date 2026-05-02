def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    lkup = {}
    for v in values:
        if lkup.get(v) is None:
            lkup[v] = 1
        else:
            lkup[v] += 1

    srt_values = sorted(values)

    i = 0
    while i < len(srt_values):
        cnt = lkup[srt_values[i]]
        avg = cnt * (i + i + cnt + 1) / (2.0 * cnt)
        lkup[srt_values[i]] = avg
        i += cnt
        

    return [lkup[v] for v in values]
    
    
    