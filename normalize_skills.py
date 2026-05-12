# ==========================================
# normalize_skills.py
# ==========================================

def normalize_skills(skill_text, alias_mapping):

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