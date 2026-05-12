"""
Job Description Module - Job description data and processing
"""

JDS = {
    "JD-1": {
        "company": "Kakao",
        "role": "ML Engineer",
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "SQL",
            "Data Visualization"
        ]
    },

    "JD-2": {
        "company": "Naver",
        "role": "Backend Engineer",
        "skills": [
            "Java",
            "Spring Boot",
            "MySQL",
            "Microservices",
            "Docker",
            "Kubernetes"
        ]
    },

    "JD-3": {
        "company": "Samsung",
        "role": "Data Scientist",
        "skills": [
            "Python",
            "Machine Learning",
            "Data Analysis",
            "SQL",
            "Statistics"
        ]
    }
}


def process_job_description(jd_id, jd_data, alias_mapping):
    """
    Process a single job description.
    
    Args:
        jd_id (str): Job description ID
        jd_data (dict): Job description data with 'company', 'role', 'skills'
        alias_mapping (dict): Skill aliases
    
    Returns:
        dict: Processed JD with company, role, and normalized skills
    """
    from resume import normalize_skills, deduplicate_skills
    
    jd_skill_string = ",".join(jd_data["skills"])
    normalized_skills = normalize_skills(jd_skill_string, alias_mapping)
    unique_skills = deduplicate_skills(normalized_skills)
    
    return {
        "jd_id": jd_id,
        "company": jd_data["company"],
        "role": jd_data["role"],
        "skills": unique_skills
    }


def process_all_jds(jds_dict, alias_mapping):
    """
    Process all job descriptions.
    
    Args:
        jds_dict (dict): Dictionary of jd_id -> jd_data
        alias_mapping (dict): Skill aliases
    
    Returns:
        dict: Dictionary of jd_id -> processed_jd
    """
    processed = {}
    for jd_id, jd_data in jds_dict.items():
        processed[jd_id] = process_job_description(jd_id, jd_data, alias_mapping)
    return processed
