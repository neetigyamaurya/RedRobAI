"""
Resume Module - Resume data and processing
"""

RESUMES = {
    "Sneha Singh":
        "Python, MachineLearning, SQL, pandas, numpy, Deep-learning",

    "Meera Kapoor":
        "JavaScript, ReactJS, Node.JS, MongoDB, REST API, HTML/CSS",

    "Karan Malhotra":
        "Java, Spring Boot, MySQL, Microservices, Docker, Kubernetes"
}


def normalize_skills(skill_text, alias_mapping):
    """
    Normalize skill names using alias mapping.
    
    Args:
        skill_text (str): Comma-separated skill string
        alias_mapping (dict): Dictionary mapping skills to canonical names
    
    Returns:
        list: List of normalized skill names
    """
    skill_text = skill_text.lower()
    raw_tokens = skill_text.split(",")
    normalized = []

    for token in raw_tokens:
        token = token.strip()
        if token in alias_mapping:
            canonical_skill = alias_mapping[token]
            normalized.append(canonical_skill)

    return normalized


def deduplicate_skills(skills):
    """
    Remove duplicate skills from a list.
    
    Args:
        skills (list): List of skill names
    
    Returns:
        list: List of unique skill names
    """
    unique_skills = []
    for skill in skills:
        if skill not in unique_skills:
            unique_skills.append(skill)
    return unique_skills


def process_resume(candidate_name, resume_text, alias_mapping):
    """
    Process a single resume - normalize and deduplicate skills.
    
    Args:
        candidate_name (str): Name of the candidate
        resume_text (str): Raw skill text from resume
        alias_mapping (dict): Skill aliases
    
    Returns:
        tuple: (candidate_name, processed_skills)
    """
    normalized = normalize_skills(resume_text, alias_mapping)
    unique = deduplicate_skills(normalized)
    return candidate_name, unique


def process_all_resumes(resumes_dict, alias_mapping):
    """
    Process all resumes.
    
    Args:
        resumes_dict (dict): Dictionary of candidate_name -> resume_text
        alias_mapping (dict): Skill aliases
    
    Returns:
        dict: Dictionary of candidate_name -> processed_skills
    """
    processed = {}
    for candidate_name, resume_text in resumes_dict.items():
        _, skills = process_resume(candidate_name, resume_text, alias_mapping)
        processed[candidate_name] = skills
    return processed
