"""
Matcher Module - TF-IDF vectorization and candidate ranking
"""

import math


def build_vocabulary(all_resume_skills):
    """
    Build vocabulary from all resume skills.
    
    Args:
        all_resume_skills (list): List of skill lists from all resumes
    
    Returns:
        list: Sorted list of unique skills
    """
    vocabulary = []
    for skills in all_resume_skills:
        for skill in skills:
            if skill not in vocabulary:
                vocabulary.append(skill)
    vocabulary.sort()
    return vocabulary


def compute_tf(skills, vocabulary):
    """
    Compute term frequency vector.
    
    Args:
        skills (list): List of skills
        vocabulary (list): Complete vocabulary list
    
    Returns:
        list: TF vector where each value is 1/total_skills or 0
    """
    tf_vector = []
    total_unique_skills = len(skills)

    for vocab_word in vocabulary:
        if vocab_word in skills:
            tf = 1 / total_unique_skills
        else:
            tf = 0
        tf_vector.append(tf)

    return tf_vector


def compute_idf(all_resume_skills, vocabulary):
    """
    Compute inverse document frequency vector.
    
    Args:
        all_resume_skills (list): List of skill lists from all resumes
        vocabulary (list): Complete vocabulary list
    
    Returns:
        list: IDF vector using natural logarithm
    """
    total_documents = len(all_resume_skills)
    idf_vector = []

    for vocab_word in vocabulary:
        document_frequency = 0
        for skills in all_resume_skills:
            if vocab_word in skills:
                document_frequency += 1

        idf = math.log(total_documents / document_frequency)
        idf_vector.append(idf)

    return idf_vector


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


def build_resume_vectors(processed_resumes, vocabulary, idf_vector):
    """
    Build TF-IDF vectors for all resumes.
    
    Args:
        processed_resumes (dict): Dictionary of candidate_name -> skills
        vocabulary (list): Complete vocabulary list
        idf_vector (list): IDF vector
    
    Returns:
        dict: Dictionary of candidate_name -> tfidf_vector
    """
    resume_vectors = {}

    for candidate_name, skills in processed_resumes.items():
        tf_vector = compute_tf(skills, vocabulary)
        tfidf_vector = compute_tfidf(tf_vector, idf_vector)
        resume_vectors[candidate_name] = tfidf_vector

    return resume_vectors


def rank_candidates(resume_vectors, jd_vector):
    """
    Rank candidates based on similarity to job description.
    
    Args:
        resume_vectors (dict): Dictionary of candidate_name -> vector
        jd_vector (list): Job description vector
    
    Returns:
        list: Top 3 candidates as (name, score) tuples, sorted by score descending
    """
    scores = []

    for candidate_name in resume_vectors:
        vector = resume_vectors[candidate_name]
        similarity = cosine_similarity(vector, jd_vector)
        scores.append((candidate_name, similarity))

    scores.sort(key=lambda x: (-x[1], x[0]))
    return scores[:3]


def match_candidates_to_jd(processed_resumes, vocabulary, idf_vector, jd_skills):
    """
    Match candidates to a specific job description.
    
    Args:
        processed_resumes (dict): Dictionary of candidate_name -> skills
        vocabulary (list): Complete vocabulary list
        idf_vector (list): IDF vector
        jd_skills (list): Skills in the job description
    
    Returns:
        list: Ranked candidates as (name, score) tuples
    """
    resume_vectors = build_resume_vectors(
        processed_resumes,
        vocabulary,
        idf_vector
    )

    jd_vector = build_jd_vector(jd_skills, vocabulary)
    rankings = rank_candidates(resume_vectors, jd_vector)

    return rankings
