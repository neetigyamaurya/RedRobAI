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

- `main.py`: Main script that orchestrates the entire matching process
- `normalize_skills.py`: Normalizes skill names using aliases
- `deduplicate_skills.py`: Removes duplicate skills
- `build_vocabulary.py`: Creates vocabulary from all resume skills
- `compute_tf.py`: Computes term frequency vectors
- `compute_idf.py`: Computes inverse document frequency
- `compute_tfidf.py`: Combines TF and IDF into TF-IDF vectors
- `build_jd_vector.py`: Builds TF-IDF vectors for job descriptions
- `rank_candidates.py`: Ranks candidates using cosine similarity
- `resumes.py`: Sample resume data
- `jds.py`: Sample job description data
- `skill_aliases.py`: Skill name aliases for normalization

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/job-matching-system.git
   cd job-matching-system
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. No additional dependencies are required (uses only Python standard library).

## Usage

Run the main script:
```bash
python main.py
```

The system will process the sample resumes and job descriptions, then output ranked candidate lists for each job opening.

## Example Output

```
JD-1 - Kakao (ML Engineer)
Arjun Sharma (0.83)
Karan Mehta (0.37)
Sneha Patel (0.28)

JD-2 - Naver (Backend Engineer)
Rahul Gupta (1.0)
Arjun Sharma (0.0)
Karan Mehta (0.0)
```

## Sample Data

The project includes sample data:
- **Resumes**: 5 candidates with various technical skills
- **Job Descriptions**: 2 positions (ML Engineer and Backend Engineer)
- **Skill Aliases**: Common variations of skill names

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

To use your own data:
- Edit `resumes.py` with your candidate data
- Edit `jds.py` with your job descriptions
- Update `skill_aliases.py` with relevant skill mappings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).