"""
Example usage of the job_matching_system module
"""

from job_matching_system import (
    normalize_skills,
    deduplicate_skills,
    build_vocabulary,
    compute_tf,
    compute_idf,
    compute_tfidf,
    build_jd_vector,
    rank_candidates,
    SKILL_ALIASES,
    RESUMES,
    JDS,
)


def main():
    """Main function demonstrating the job matching system"""
    
    # ==========================================
    # Normalize + Deduplicate Resumes
    # ==========================================
    
    processed_resumes = {}
    
    for candidate_name in RESUMES:
    
        raw_skill_text = RESUMES[candidate_name]
    
        normalized_skills = normalize_skills(
            raw_skill_text,
            SKILL_ALIASES
        )
    
        unique_skills = deduplicate_skills(
            normalized_skills
        )
    
        processed_resumes[candidate_name] = unique_skills
    
    
    # ==========================================
    # Build Vocabulary
    # ==========================================
    
    all_resume_skills = list(
        processed_resumes.values()
    )
    
    vocabulary = build_vocabulary(
        all_resume_skills
    )
    
    
    # ==========================================
    # Compute IDF
    # ==========================================
    
    idf_vector = compute_idf(
        all_resume_skills,
        vocabulary
    )
    
    
    # ==========================================
    # Build Resume TF-IDF Vectors
    # ==========================================
    
    resume_vectors = {}
    
    for candidate_name in processed_resumes:
    
        skills = processed_resumes[candidate_name]
    
        tf_vector = compute_tf(
            skills,
            vocabulary
        )
    
        tfidf_vector = compute_tfidf(
            tf_vector,
            idf_vector
        )
    
        resume_vectors[candidate_name] = tfidf_vector
    
    
    # ==========================================
    # Process JDs
    # ==========================================
    
    for jd_id in JDS:
    
        jd_data = JDS[jd_id]
    
        company = jd_data["company"]
        role = jd_data["role"]
    
        jd_skill_string = ",".join(
            jd_data["skills"]
        )
    
        normalized_jd_skills = normalize_skills(
            jd_skill_string,
            SKILL_ALIASES
        )
    
        normalized_jd_skills = deduplicate_skills(
            normalized_jd_skills
        )
    
        jd_vector = build_jd_vector(
            normalized_jd_skills,
            vocabulary
        )
    
        rankings = rank_candidates(
            resume_vectors,
            jd_vector
        )
    
        print()
    
        print(
            jd_id,
            "-",
            company,
            "(" + role + ")"
        )
    
        for candidate_name, score in rankings:
    
            rounded_score = round(
                score,
                2
            )
    
            print(
                candidate_name,
                "(" + str(rounded_score) + ")"
            )


if __name__ == "__main__":
    main()
