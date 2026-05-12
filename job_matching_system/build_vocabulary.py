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
