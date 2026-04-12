import numpy as np

def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    # Write code here
    if not s1 or not s2:
        return max(len(s1), len(s2))

        
    dp = np.zeros((len(s1) + 1, len(s2) + 1), dtype=int)
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for j in range(len(s2) + 1):
        dp[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                print(dp[i][j])
            else:
                dp[i][j] = 1 + min(dp[i-1][j], 
                                   dp[i][j-1], 
                                   dp[i-1][j-1])
    print(dp)
    res = dp[len(s1)][len(s2)]
    return int(res)
                