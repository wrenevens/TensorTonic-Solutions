def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    N = len(values)
    left = 0
    right = N - 1
    for i in range(N):
        if values[i] is None:
            while left < i - 1:
                left += 1
            while right > i + 1 and values[right - 1] != None:
                right -= 1

            values[i] = values[left] + (i - left) / (right - left) * (values[right] - values[left])
    return values
            
                
            