# Job Matching System

A Python-based system that matches job candidates to job descriptions using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization and cosine similarity scoring.

## Overview

This project processes resumes and job descriptions to:
- Normalize and deduplicate skills using predefined aliases
- Build a vocabulary from all resume skills
- Compute TF-IDF vectors for resumes and job descriptions
- Rank candidates for each job opening based on similarity scores

## Features

- **Skill Normalization**: Standardizes skill names using aliases (e.g., "MachineLearning" → "Machine Learning")
- **Deduplication**: Removes duplicate skills from resumes
- **TF-IDF Vectorization**: Converts skills into numerical vectors for comparison
- **Cosine Similarity Ranking**: Scores and ranks candidates by relevance to job requirements

## Project Structure

```
project/
├── main.py              # Entry point - orchestrates the workflow
├── skill_aliases.py     # Skill name mappings
├── resume.py           # Resume data & processing functions
├── job_description.py  # Job description data & processing
└── matcher.py          # TF-IDF vectorization & ranking logic
```

### File Descriptions

- **main.py**: Entry point that orchestrates the entire workflow
  - Processes resumes, job descriptions
  - Builds vocabulary and computes IDF
  - Ranks candidates for each job

- **skill_aliases.py**: Contains skill name mappings
  - Maps skill variations to canonical names (e.g., "MachineLearning" → "machine_learning")

- **resume.py**: Resume data and processing
  - Contains sample resume data (3 candidates)
  - Functions: `normalize_skills()`, `deduplicate_skills()`, `process_all_resumes()`

- **job_description.py**: Job description data and processing
  - Contains sample job descriptions (3 positions)
  - Functions: `process_job_description()`, `process_all_jds()`

- **matcher.py**: Core matching logic
  - TF-IDF vectorization: `compute_tf()`, `compute_idf()`, `compute_tfidf()`
  - Similarity computation: `cosine_similarity()`, `dot_product()`, `magnitude()`
  - Ranking: `rank_candidates()`, `match_candidates_to_jd()`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/neetigyamaurya/RedRobAI.git
   cd RedRobAI
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. No additional dependencies are required (uses only Python standard library).

## Quick Start

```bash
cd project
python main.py
```

This will run the job matching system with sample data and display rankings.

## Usage

Run the main script from the project directory:
```bash
cd project
python main.py
```

The system will process the sample resumes and job descriptions, then output ranked candidate lists for each job opening.

## Example Output

```
==================================================
JOB MATCHING SYSTEM
==================================================

[1/5] Processing resumes...
  ✓ Processed 3 resumes
[2/5] Processing job descriptions...
  ✓ Processed 3 job descriptions
[3/5] Building vocabulary...
  ✓ Built vocabulary with 14 unique skills
[4/5] Computing IDF...
  ✓ IDF computed
[5/5] Ranking candidates for each job...

JD-1 - Kakao (ML Engineer)
  → Sneha Singh (1.0)
  → Karan Malhotra (0.0)
  → Meera Kapoor (0.0)

JD-2 - Naver (Backend Engineer)
  → Karan Malhotra (1.0)
  → Meera Kapoor (0.0)
  → Sneha Singh (0.0)

JD-3 - Samsung (Data Scientist)
  → Sneha Singh (0.87)
  → Karan Malhotra (0.0)
  → Meera Kapoor (0.0)

==================================================
Matching complete!
==================================================
```

## Sample Data

The project includes sample data:
- **Resumes**: 3 candidates (Sneha Singh, Meera Kapoor, Karan Malhotra)
- **Job Descriptions**: 3 positions
  - Kakao: ML Engineer
  - Naver: Backend Engineer
  - Samsung: Data Scientist
- **Skill Aliases**: Common variations of skill names (30+ mappings)

## Algorithm Details

1. **Preprocessing**:
   - Normalize skills using aliases
   - Deduplicate skills in each resume

2. **Vocabulary Building**:
   - Collect all unique skills across resumes

3. **TF-IDF Computation**:
   - TF: Term frequency in each document
   - IDF: Inverse document frequency across corpus
   - TF-IDF: Product of TF and IDF

4. **Matching**:
   - Build TF-IDF vector for each job description
   - Compute cosine similarity between JD vector and each resume vector
   - Rank candidates by similarity score (higher is better)

## Customization

To use your own data, edit the files in the `project/` directory:
- **project/resume.py**: Update `RESUMES` dictionary with your candidate data
- **project/job_description.py**: Update `JDS` dictionary with your job descriptions
- **project/skill_aliases.py**: Add or update skill name mappings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).