def dot_product(vec1, vec2):

    total = 0

    for i in range(len(vec1)):

        total += vec1[i] * vec2[i]

    return total