from unittest import TestCase
from A2.dungeonsanddragons import generate_vowel


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

    def test_generate_vowel_type(self):
        expected = str
        actual = type(generate_vowel())
        self.assertEqual(expected, actual)