def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1, y1, x2, y2 = box_a
    area_a = (x2 - x1) * (y2 - y1)
    
    m1, n1, m2, n2 = box_b
    area_b = (m2 - m1) * (n2 - n1)
    
    is_intersect = ((x1 > m2 and y1 > n2) or (x2 < m1 and y2 < n1))
    
    if (area_a == 0 and area_b == 0) or is_intersect:
        return 0.0

    minX2 = min(m2, x2)
    maxX1 = max(m1, x1)

    minY2 = min(n2, y2)
    maxY1 = max(n1, y1)
    
    area_intersection = (minX2 - maxX1) * (minY2 - maxY1)
    area_union = area_a + area_b - area_intersection
    return area_intersection / area_union

    

    
        
        
        
    