import math
import itertools

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride = image_size / feature_size
    combinators = itertools.product(scales, aspect_ratios)
    box = [(s*math.sqrt(r), s/math.sqrt(r)) for s, r in combinators]
    
    result = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride
            for _w, _h in box:
                result.append([cx - _w/2, cy - _h/2, cx + _w/2, cy + _h/2])
    return result

    
            