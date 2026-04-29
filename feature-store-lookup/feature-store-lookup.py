def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    result = []
    for req in requests:
        user_id = req['user_id']
        online_features = req['online_features']

        if feature_store.get(user_id) is None:
            result.append(defaults | online_features)
        else:
            result.append(feature_store[user_id] | online_features)
    return result

            