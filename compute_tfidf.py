def compute_tfidf(tf_vector, idf_vector):

    tfidf_vector = []

    for i in range(len(tf_vector)):

        tfidf = tf_vector[i] * idf_vector[i]

        tfidf_vector.append(tfidf)

    return tfidf_vector