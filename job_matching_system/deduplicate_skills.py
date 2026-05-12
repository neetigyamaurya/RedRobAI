def deduplicate_skills(skills):
    """
    Remove duplicate skills from a list.
    
    Args:
        skills (list): List of skill names
    
    Returns:
        list: List of unique skill names preserving order
    """
    unique_skills = []

    for skill in skills:

        if skill not in unique_skills:
            unique_skills.append(skill)

    return unique_skills
