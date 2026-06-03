def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here
    match mode:
        case "user":
            for user in ratings_matrix:
                mean = 0.0
                none_cnt = len(user)
                for item in user:
                    if item != 0:
                        mean += item
                        none_cnt -= 1
                if none_cnt == len(user):
                    continue
                mean /= (len(user) - none_cnt)
                for i in range(len(user)):
                    if user[i] == 0:
                        user[i] = mean
                        none_cnt -= 1
                    if not none_cnt:
                        break
            return ratings_matrix
                
        case "item":
            items_len = len(ratings_matrix[0])
            for item in range(items_len):
                mean = 0.0
                none_cnt = len(ratings_matrix)
                for user in range(len(ratings_matrix)):
                    if ratings_matrix[user][item] != 0:
                        mean += ratings_matrix[user][item]
                        none_cnt -= 1
                if len(ratings_matrix) == none_cnt:
                    continue
                mean /= (len(ratings_matrix) - none_cnt)

                for user in range(len(ratings_matrix)):
                    if ratings_matrix[user][item] == 0:
                        ratings_matrix[user][item] = mean
            return ratings_matrix
                    
                    