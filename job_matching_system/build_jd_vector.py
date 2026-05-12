def build_jd_vector(jd_skills, vocabulary):
    """
    Build binary vector for job description skills.
    
    Args:
        jd_skills (list): List of skills in the job description
        vocabulary (list): Complete vocabulary list
    
    Returns:
        list: Binary vector (1 if skill present, 0 otherwise)
    """
    vector = []

    for vocab_word in vocabulary:

        if vocab_word in jd_skills:
            vector.append(1)

        else:
            vector.append(0)

    return vector
