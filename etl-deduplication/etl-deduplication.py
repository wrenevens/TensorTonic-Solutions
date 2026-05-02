def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    # Write code here
    def get_hashed_keys(record):
        keys = []
        for k in key_columns:
            keys.append(record[k])
        return hash(tuple(keys))
        
    def first_strat():
        lkup = {}
        for record in records:
            hashed_keys = get_hashed_keys(record)
            if lkup.get(hashed_keys) is None:
                lkup[hashed_keys] = record
        return list(lkup.values())
        
            
    def last_strat():
        lkup = {}
        for record in records:
            hashed_keys = get_hashed_keys(record)
            lkup[hashed_keys] = record
        return list(lkup.values())
               
        
    def most_complete_strat():
        lkup = {}
        for record in records:
            none_cnts = 0
            for key in record.keys():
                none_cnts += 1 if record[key] is None else 0
            hashed_keys = get_hashed_keys(record)
            if lkup.get(hashed_keys) is None:
                lkup[hashed_keys] = [record, none_cnts]
            else:
                if none_cnts < lkup[hashed_keys][1]:
                    lkup[hashed_keys][0] = record
        return [v[0] for v in lkup.values()]
        
    match strategy:
        case "first":
            return first_strat()
        case "last":
            return last_strat()
        case "most_complete":
            return most_complete_strat()