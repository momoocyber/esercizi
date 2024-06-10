import unittest
from lezione15 import anagram


class TestAnagram(unittest.TestCase):
    
    def test_anagrams(self):
        self.assertTrue(anagram("listen", "silent"))
        self.assertTrue(anagram("Triangle", "Integral"))
        self.assertTrue(anagram("apple", "paleP"))
        self.assertTrue(anagram("anagram", "nagaram"))

    def test_not_anagrams(self):
        self.assertFalse(anagram("hello", "world"))
        self.assertFalse(anagram("apple", "pale"))
        self.assertFalse(anagram("rat", "car"))
        self.assertFalse(anagram("one", "two"))
    
    def test_case_insensitivity(self):
        self.assertTrue(anagram("Listen", "Silent"))
        self.assertTrue(anagram("Triangle", "Integral"))
    
    def test_empty_strings(self):
        self.assertTrue(anagram("", ""))
    
    def test_different_lengths(self):
        self.assertFalse(anagram("a", "ab"))
        self.assertFalse(anagram("ab", "abc"))

# Run the tests
if __name__ == "__main__":
    unittest.main()

