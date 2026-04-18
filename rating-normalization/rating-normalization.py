def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    for r in range(len(matrix)):
        counts_no_zeros = len(matrix[r])
        sum_row = 0.0
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                counts_no_zeros -= 1
            sum_row += matrix[r][c]
        if counts_no_zeros == 0:
            continue
        mean_row = sum_row / counts_no_zeros
        matrix[r] = [v - mean_row if v != 0.0 else 0.0 for v in matrix[r]]
        
    return matrix