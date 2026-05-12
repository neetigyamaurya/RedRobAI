# ==========================================
# compute_tf.py
# ==========================================

def compute_tf(skills, vocabulary):

    tf_vector = []

    total_unique_skills = len(skills)

    for vocab_word in vocabulary:

        if vocab_word in skills:

            tf = 1 / total_unique_skills

        else:
            tf = 0

        tf_vector.append(tf)

    return tf_vector