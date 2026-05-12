# ==========================================
# compute_idf.py
# ==========================================

import math


def compute_idf(all_resume_skills, vocabulary):

    total_documents = len(
        all_resume_skills
    )

    idf_vector = []

    for vocab_word in vocabulary:

        document_frequency = 0

        for skills in all_resume_skills:

            if vocab_word in skills:
                document_frequency += 1

        # Natural logarithm
        idf = math.log(
            total_documents / document_frequency
        )

        idf_vector.append(idf)

    return idf_vector