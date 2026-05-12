"""
Main Module - Job Matching System Entry Point

This module orchestrates the job matching workflow:
1. Process resumes (normalize and deduplicate skills)
2. Process job descriptions (normalize and deduplicate skills)
3. Build vocabulary and compute IDF
4. Rank candidates for each job
"""

from skill_aliases import SKILL_ALIASES
from resume import RESUMES, process_all_resumes
from job_description import JDS, process_all_jds
from matcher import (
    build_vocabulary,
    compute_idf,
    match_candidates_to_jd
)


def main():
    """Main function that orchestrates the job matching system"""

    print("=" * 50)
    print("JOB MATCHING SYSTEM")
    print("=" * 50)

    # ==========================================
    # Step 1: Process Resumes
    # ==========================================
    print("\n[1/5] Processing resumes...")
    processed_resumes = process_all_resumes(RESUMES, SKILL_ALIASES)
    print(f"  ✓ Processed {len(processed_resumes)} resumes")

    # ==========================================
    # Step 2: Process Job Descriptions
    # ==========================================
    print("[2/5] Processing job descriptions...")
    processed_jds = process_all_jds(JDS, SKILL_ALIASES)
    print(f"  ✓ Processed {len(processed_jds)} job descriptions")

    # ==========================================
    # Step 3: Build Vocabulary
    # ==========================================
    print("[3/5] Building vocabulary...")
    all_resume_skills = list(processed_resumes.values())
    vocabulary = build_vocabulary(all_resume_skills)
    print(f"  ✓ Built vocabulary with {len(vocabulary)} unique skills")

    # ==========================================
    # Step 4: Compute IDF
    # ==========================================
    print("[4/5] Computing IDF...")
    idf_vector = compute_idf(all_resume_skills, vocabulary)
    print("  ✓ IDF computed")

    # ==========================================
    # Step 5: Rank Candidates for Each JD
    # ==========================================
    print("[5/5] Ranking candidates for each job...\n")

    for jd_id, jd_data in processed_jds.items():
        company = jd_data["company"]
        role = jd_data["role"]
        jd_skills = jd_data["skills"]

        rankings = match_candidates_to_jd(
            processed_resumes,
            vocabulary,
            idf_vector,
            jd_skills
        )

        print(f"{jd_id} - {company} ({role})")
        for candidate_name, score in rankings:
            rounded_score = round(score, 2)
            print(f"  → {candidate_name} ({rounded_score})")
        print()

    print("=" * 50)
    print("Matching complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
