# ==========================================
# normalize_skills.py
# ==========================================

def normalize_skills(skill_text, alias_mapping):
    """
    Normalize skill names using alias mapping.
    
    Args:
        skill_text (str): Comma-separated skill string
        alias_mapping (dict): Dictionary mapping skills to canonical names
    
    Returns:
        list: List of normalized skill names
    """
    # Convert to lowercase
    skill_text = skill_text.lower()

    # Split on commas
    raw_tokens = skill_text.split(",")

    normalized = []

    for token in raw_tokens:

        # Remove extra spaces
        token = token.strip()

        # Apply alias mapping
        if token in alias_mapping:

            canonical_skill = alias_mapping[token]

            normalized.append(canonical_skill)

    return normalized
