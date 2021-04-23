from unittest import TestCase
from Lab05.lab05 import generate_consonant


class TestGenerateConsonant(TestCase):
    def test_generate_consonant_one(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        consonant = generate_consonant()
        self.assertIn(consonant, consonants)

    def test_generate_consonant_two(self):
        not_consonants = "aeiou"
        consonant = generate_consonant()
        self.assertNotIn(consonant, not_consonants)

    def test_generate_consonant_three(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        consonant = generate_consonant()
        self.assertTrue(consonant in consonants)

    def test_generate_consonant_four(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        consonant = generate_consonant()
        self.assertFalse(consonant not in consonants)
