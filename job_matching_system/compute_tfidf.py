def compute_tfidf(tf_vector, idf_vector):
    """
    Compute TF-IDF vector by multiplying TF and IDF.
    
    Args:
        tf_vector (list): Term frequency vector
        idf_vector (list): Inverse document frequency vector
    
    Returns:
        list: TF-IDF vector (element-wise multiplication)
    """
    tfidf_vector = []

    for i in range(len(tf_vector)):

        tfidf = tf_vector[i] * idf_vector[i]

        tfidf_vector.append(tfidf)

    return tfidf_vector
