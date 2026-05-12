# ==========================================
# rank_candidates.py
# ==========================================

from .cosine_similarity import cosine_similarity


def rank_candidates(
    resume_vectors,
    jd_vector
):
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

        vector = resume_vectors[
            candidate_name
        ]

        similarity = cosine_similarity(
            vector,
            jd_vector
        )

        scores.append(
            (
                candidate_name,
                similarity
            )
        )

    # Sort:
    # 1. Higher score first
    # 2. Alphabetical tie-break

    scores.sort(
        key=lambda x: (
            -x[1],
            x[0]
        )
    )

    return scores[:3]
