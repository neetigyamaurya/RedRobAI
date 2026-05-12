def dot_product(vec1, vec2):
    """
    Compute dot product of two vectors.
    
    Args:
        vec1 (list): First vector
        vec2 (list): Second vector
    
    Returns:
        float: Dot product result
    """
    total = 0

    for i in range(len(vec1)):

        total += vec1[i] * vec2[i]

    return total
