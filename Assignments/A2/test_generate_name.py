from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import generate_name


class TestGenerateName(TestCase):

    def test_generate_name_negative(self):
        expected = ""
        actual = generate_name(-1)
        self.assertEqual(expected, actual)

    def test_generate_name_zero(self):
        expected = ""
        actual = generate_name(0)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["c", "a", "n", "a", "d", "a"])
    def test_generate_name_three(self, mock_value):
        expected = "Canada"
        actual = generate_name(3)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["b", "a"])
    def test_generate_name_one(self, mock_value):
        expected = "Ba"
        actual = generate_name(1)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["b", "a", "c", "e"])
    def test_generate_name_two(self, mock_value):
        expected = "Bace"
        actual = generate_name(2)
        self.assertEqual(expected, actual)

    def test_generate_name_type(self):
        expected = str
        actual = type(generate_name(2))
        self.assertEqual(expected, actual)
