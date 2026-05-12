def build_vocabulary(all_resume_skills):

    vocabulary = []

    for skills in all_resume_skills:

        for skill in skills:

            if skill not in vocabulary:
                vocabulary.append(skill)

    vocabulary.sort()

    return vocabulary