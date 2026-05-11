def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    grayscale = []

    for row in image:
        gray_row = []
        for pixel in row:
            gray_pixel = pixel[0] * 0.299
            gray_pixel += pixel[1] * 0.587
            gray_pixel += pixel[2] * 0.114
            gray_row.append(gray_pixel)
        grayscale.append(gray_row)
    return grayscale
            