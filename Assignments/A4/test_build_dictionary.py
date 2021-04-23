from unittest import TestCase
from A4.question_7 import build_dictionary
from unittest.mock import patch


class TestBuildDictionary(TestCase):
    @patch('builtins.input', side_effect=['q'])
    def test_build_dictionary(self, mock_input):
        expected = None
        actual = build_dictionary()
        self.assertEqual(expected, actual)
