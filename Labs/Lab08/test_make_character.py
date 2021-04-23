from unittest import TestCase
from Lab08.maze import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {"x": 0, "y": 0}
        actual = make_character()
        self.assertEqual(expected, actual)
