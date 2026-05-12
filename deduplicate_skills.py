def deduplicate_skills(skills):

    unique_skills = []

    for skill in skills:

        if skill not in unique_skills:
            unique_skills.append(skill)

    return unique_skills