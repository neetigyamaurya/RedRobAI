def magnitude(vec):
    """
    Compute magnitude (Euclidean norm) of a vector.
    
    Args:
        vec (list): Input vector
    
    Returns:
        float: Magnitude of the vector
    """
    total = 0

    for value in vec:

        total += value * value

    return total ** 0.5
