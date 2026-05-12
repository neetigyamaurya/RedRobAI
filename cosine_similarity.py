from dot_product import dot_product
from magnitude import magnitude


def cosine_similarity(vec1, vec2):

    dp = dot_product(vec1, vec2)

    mag1 = magnitude(vec1)
    mag2 = magnitude(vec2)

    if mag1 == 0 or mag2 == 0:
        return 0

    similarity = dp / (mag1 * mag2)

    return similarity