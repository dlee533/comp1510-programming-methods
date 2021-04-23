from unittest import TestCase
from Lab05.lab05 import generate_vowel


class TestGenerateVowel(TestCase):

    def test_generate_vowel_one(self):
        vowels = "aeiouy"
        vowel = generate_vowel()
        self.assertIn(vowel, vowels)

    def test_generate_vowel_two(self):
        not_vowels = "bcdfghjklmnpqrstvwxz"
        vowel = generate_vowel()
        self.assertNotIn(not_vowels, vowel)

    def test_generate_vowel_three(self):
        vowels = "aeiouy"
        vowel = generate_vowel()
        self.assertTrue(vowel in vowels)

    def test_generate_vowel_four(self):
        vowels = "aeiouy"
        vowel = generate_vowel()
        self.assertFalse(vowel not in vowels)
