def build_jd_vector(jd_skills, vocabulary):

    vector = []

    for vocab_word in vocabulary:

        if vocab_word in jd_skills:
            vector.append(1)

        else:
            vector.append(0)

    return vector