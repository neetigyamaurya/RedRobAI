from .dot_product import dot_product
from .magnitude import magnitude


def cosine_similarity(vec1, vec2):
    """
    Compute cosine similarity between two vectors.
    
    Args:
        vec1 (list): First vector
        vec2 (list): Second vector
    
    Returns:
        float: Cosine similarity in range [-1, 1]
    """
    dp = dot_product(vec1, vec2)

    mag1 = magnitude(vec1)
    mag2 = magnitude(vec2)

    if mag1 == 0 or mag2 == 0:
        return 0

    similarity = dp / (mag1 * mag2)

    return similarity
