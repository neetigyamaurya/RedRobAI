"""
Job Matching System Module

A Python-based system that matches job candidates to job descriptions 
using TF-IDF vectorization and cosine similarity scoring.

Main functions:
- normalize_skills: Normalize and standardize skill names
- deduplicate_skills: Remove duplicate skills
- build_vocabulary: Create vocabulary from all skills
- compute_tf: Calculate term frequency
- compute_idf: Calculate inverse document frequency
- compute_tfidf: Combine TF and IDF
- cosine_similarity: Calculate vector similarity
- rank_candidates: Rank candidates for a job description
"""

from .normalize_skills import normalize_skills
from .deduplicate_skills import deduplicate_skills
from .build_vocabulary import build_vocabulary
from .compute_tf import compute_tf
from .compute_idf import compute_idf
from .compute_tfidf import compute_tfidf
from .build_jd_vector import build_jd_vector
from .rank_candidates import rank_candidates
from .cosine_similarity import cosine_similarity
from .dot_product import dot_product
from .magnitude import magnitude
from .skill_aliases import SKILL_ALIASES
from .resumes import RESUMES
from .jds import JDS

__version__ = "1.0.0"
__all__ = [
    "normalize_skills",
    "deduplicate_skills",
    "build_vocabulary",
    "compute_tf",
    "compute_idf",
    "compute_tfidf",
    "build_jd_vector",
    "rank_candidates",
    "cosine_similarity",
    "dot_product",
    "magnitude",
    "SKILL_ALIASES",
    "RESUMES",
    "JDS",
]
