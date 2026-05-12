import unittest
from job_matching_system.normalize_skills import normalize_skills
from job_matching_system.deduplicate_skills import deduplicate_skills
from job_matching_system.build_vocabulary import build_vocabulary
from job_matching_system.compute_tf import compute_tf
from job_matching_system.compute_idf import compute_idf
from job_matching_system.compute_tfidf import compute_tfidf
from job_matching_system.build_jd_vector import build_jd_vector
from job_matching_system.rank_candidates import rank_candidates
from job_matching_system.cosine_similarity import cosine_similarity
from job_matching_system.dot_product import dot_product
from job_matching_system.magnitude import magnitude


class TestNormalizeSkills(unittest.TestCase):
    """Test cases for normalize_skills function"""
    
    def setUp(self):
        self.alias_mapping = {
            "machinelearning": "Machine Learning",
            "python": "Python",
            "sql": "SQL"
        }
    
    def test_normalize_basic(self):
        """Test basic skill normalization"""
        result = normalize_skills("Python, SQL", self.alias_mapping)
        self.assertIn("Python", result)
        self.assertIn("SQL", result)
    
    def test_normalize_case_insensitive(self):
        """Test that normalization is case insensitive"""
        result = normalize_skills("PYTHON, sql", self.alias_mapping)
        self.assertEqual(len(result), 2)
    
    def test_normalize_with_spaces(self):
        """Test normalization with extra spaces"""
        result = normalize_skills("  Python  ,  SQL  ", self.alias_mapping)
        self.assertIn("Python", result)
        self.assertIn("SQL", result)
    
    def test_normalize_empty_string(self):
        """Test with empty string"""
        result = normalize_skills("", self.alias_mapping)
        self.assertEqual(result, [])
    
    def test_normalize_unknown_skills(self):
        """Test with unknown skills (not in mapping)"""
        result = normalize_skills("UnknownSkill, Python", self.alias_mapping)
        self.assertIn("Python", result)
        self.assertNotIn("UnknownSkill", result)


class TestDeduplicateSkills(unittest.TestCase):
    """Test cases for deduplicate_skills function"""
    
    def test_deduplicate_basic(self):
        """Test basic deduplication"""
        skills = ["Python", "SQL", "Python", "Java"]
        result = deduplicate_skills(skills)
        self.assertEqual(len(result), 3)
    
    def test_deduplicate_no_duplicates(self):
        """Test with no duplicates"""
        skills = ["Python", "Java", "SQL"]
        result = deduplicate_skills(skills)
        self.assertEqual(len(result), 3)
    
    def test_deduplicate_all_duplicates(self):
        """Test with all same skills"""
        skills = ["Python", "Python", "Python"]
        result = deduplicate_skills(skills)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Python")
    
    def test_deduplicate_empty_list(self):
        """Test with empty list"""
        result = deduplicate_skills([])
        self.assertEqual(result, [])


class TestBuildVocabulary(unittest.TestCase):
    """Test cases for build_vocabulary function"""
    
    def test_build_vocabulary_basic(self):
        """Test basic vocabulary building"""
        resumes = [["Python", "SQL"], ["Java", "Python"]]
        result = build_vocabulary(resumes)
        self.assertIn("Python", result)
        self.assertIn("SQL", result)
        self.assertIn("Java", result)
    
    def test_build_vocabulary_sorted(self):
        """Test that vocabulary is sorted"""
        resumes = [["Zebra", "Apple", "Banana"]]
        result = build_vocabulary(resumes)
        self.assertEqual(result, sorted(result))
    
    def test_build_vocabulary_empty(self):
        """Test with empty resumes"""
        result = build_vocabulary([])
        self.assertEqual(result, [])
    
    def test_build_vocabulary_no_duplicates(self):
        """Test that vocabulary has no duplicates"""
        resumes = [["Python", "Python"], ["Java", "Java"]]
        result = build_vocabulary(resumes)
        self.assertEqual(len(result), 2)


class TestComputeTF(unittest.TestCase):
    """Test cases for compute_tf function"""
    
    def test_compute_tf_basic(self):
        """Test basic TF computation"""
        skills = ["Python", "Java"]
        vocabulary = ["Python", "Java", "SQL"]
        result = compute_tf(skills, vocabulary)
        self.assertEqual(len(result), 3)
        self.assertAlmostEqual(result[0], 0.5)  # Python: 1/2
        self.assertAlmostEqual(result[1], 0.5)  # Java: 1/2
        self.assertEqual(result[2], 0)  # SQL: not present
    
    def test_compute_tf_empty_skills(self):
        """Test with empty skills"""
        vocabulary = ["Python", "Java"]
        result = compute_tf([], vocabulary)
        self.assertEqual(result, [0, 0])
    
    def test_compute_tf_all_present(self):
        """Test when all vocabulary is present"""
        skills = ["Python", "Java", "SQL"]
        vocabulary = ["Python", "Java", "SQL"]
        result = compute_tf(skills, vocabulary)
        expected = [1/3, 1/3, 1/3]
        for i, val in enumerate(expected):
            self.assertAlmostEqual(result[i], val)


class TestComputeIDF(unittest.TestCase):
    """Test cases for compute_idf function"""
    
    def test_compute_idf_basic(self):
        """Test basic IDF computation"""
        resumes = [["Python", "Java"], ["Python", "SQL"]]
        vocabulary = ["Python", "Java", "SQL"]
        result = compute_idf(resumes, vocabulary)
        self.assertEqual(len(result), 3)
        # Python appears in 2/2 docs: IDF = log(2/2) = 0
        # Java appears in 1/2 docs: IDF = log(2/1)
        # SQL appears in 1/2 docs: IDF = log(2/1)
        self.assertGreater(result[1], result[0])
    
    def test_compute_idf_rare_skill(self):
        """Test IDF of rare skill is higher"""
        resumes = [["Python"], ["Python"], ["Java"]]
        vocabulary = ["Python", "Java"]
        result = compute_idf(resumes, vocabulary)
        # Java is rarer, so IDF should be higher
        self.assertGreater(result[1], result[0])


class TestComputeTFIDF(unittest.TestCase):
    """Test cases for compute_tfidf function"""
    
    def test_compute_tfidf_basic(self):
        """Test basic TF-IDF computation"""
        tf = [0.5, 0.5, 0]
        idf = [0.5, 1.0, 1.5]
        result = compute_tfidf(tf, idf)
        self.assertEqual(len(result), 3)
        self.assertAlmostEqual(result[0], 0.25)  # 0.5 * 0.5
        self.assertAlmostEqual(result[1], 0.5)   # 0.5 * 1.0
        self.assertEqual(result[2], 0)  # 0 * 1.5
    
    def test_compute_tfidf_all_zeros(self):
        """Test with all zero TF"""
        tf = [0, 0, 0]
        idf = [1, 1, 1]
        result = compute_tfidf(tf, idf)
        self.assertEqual(result, [0, 0, 0])


class TestDotProduct(unittest.TestCase):
    """Test cases for dot_product function"""
    
    def test_dot_product_basic(self):
        """Test basic dot product"""
        vec1 = [1, 2, 3]
        vec2 = [4, 5, 6]
        result = dot_product(vec1, vec2)
        self.assertEqual(result, 32)  # 1*4 + 2*5 + 3*6 = 4+10+18
    
    def test_dot_product_zeros(self):
        """Test dot product with zeros"""
        vec1 = [0, 0, 0]
        vec2 = [1, 2, 3]
        result = dot_product(vec1, vec2)
        self.assertEqual(result, 0)
    
    def test_dot_product_perpendicular(self):
        """Test dot product of perpendicular vectors"""
        vec1 = [1, 0]
        vec2 = [0, 1]
        result = dot_product(vec1, vec2)
        self.assertEqual(result, 0)


class TestMagnitude(unittest.TestCase):
    """Test cases for magnitude function"""
    
    def test_magnitude_basic(self):
        """Test basic magnitude calculation"""
        vec = [3, 4]
        result = magnitude(vec)
        self.assertAlmostEqual(result, 5)  # sqrt(3^2 + 4^2) = 5
    
    def test_magnitude_zero_vector(self):
        """Test magnitude of zero vector"""
        vec = [0, 0, 0]
        result = magnitude(vec)
        self.assertEqual(result, 0)
    
    def test_magnitude_unit_vector(self):
        """Test magnitude of unit vector"""
        vec = [1, 0, 0]
        result = magnitude(vec)
        self.assertAlmostEqual(result, 1)


class TestCosineSimilarity(unittest.TestCase):
    """Test cases for cosine_similarity function"""
    
    def test_cosine_similarity_identical(self):
        """Test similarity of identical vectors"""
        vec1 = [1, 0, 0]
        vec2 = [1, 0, 0]
        result = cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(result, 1.0)
    
    def test_cosine_similarity_perpendicular(self):
        """Test similarity of perpendicular vectors"""
        vec1 = [1, 0, 0]
        vec2 = [0, 1, 0]
        result = cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(result, 0)
    
    def test_cosine_similarity_opposite(self):
        """Test similarity of opposite vectors"""
        vec1 = [1, 0]
        vec2 = [-1, 0]
        result = cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(result, -1.0)
    
    def test_cosine_similarity_zero_magnitude(self):
        """Test with zero magnitude vector"""
        vec1 = [0, 0]
        vec2 = [1, 1]
        result = cosine_similarity(vec1, vec2)
        self.assertEqual(result, 0)


class TestBuildJDVector(unittest.TestCase):
    """Test cases for build_jd_vector function"""
    
    def test_build_jd_vector_basic(self):
        """Test basic JD vector building"""
        jd_skills = ["Python", "SQL"]
        vocabulary = ["Python", "SQL", "Java"]
        result = build_jd_vector(jd_skills, vocabulary)
        self.assertEqual(len(result), 3)
        self.assertGreater(result[0], 0)  # Python should have value
        self.assertGreater(result[1], 0)  # SQL should have value
        self.assertEqual(result[2], 0)  # Java should be 0


class TestRankCandidates(unittest.TestCase):
    """Test cases for rank_candidates function"""
    
    def test_rank_candidates_basic(self):
        """Test basic ranking"""
        resume_vectors = {
            "Candidate1": [1, 0, 0],
            "Candidate2": [0, 1, 0],
            "Candidate3": [0.5, 0.5, 0]
        }
        jd_vector = [1, 0, 0]
        result = rank_candidates(resume_vectors, jd_vector)
        
        # Should return list of tuples
        self.assertEqual(len(result), 3)
        # First candidate should have highest score
        self.assertEqual(result[0][0], "Candidate1")
        self.assertGreater(result[0][1], result[1][1])
    
    def test_rank_candidates_sorted_descending(self):
        """Test that results are sorted in descending order"""
        resume_vectors = {
            "A": [0.1, 0, 0],
            "B": [0.5, 0, 0],
            "C": [0.9, 0, 0]
        }
        jd_vector = [1, 0, 0]
        result = rank_candidates(resume_vectors, jd_vector)
        
        # Scores should be in descending order
        for i in range(len(result) - 1):
            self.assertGreaterEqual(result[i][1], result[i+1][1])


if __name__ == '__main__':
    unittest.main()
