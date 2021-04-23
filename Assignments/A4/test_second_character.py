from unittest import TestCase
from A4.question_3 import second_character


class TestSecondCharacter(TestCase):
    def test_second_character_red(self):
        expected = 'e'
        actual = second_character('red')
        self.assertEqual(expected, actual)

    def test_second_character_white(self):
        expected = 'h'
        actual = second_character('white')
        self.assertEqual(expected, actual)

    def test_second_character_blue(self):
        expected = 'l'
        actual = second_character('blue')
        self.assertEqual(expected, actual)
