from unittest import TestCase
from Lab08.maze import get_user_choice
from unittest.mock import patch


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value='n')
    def test_get_user_choice_n(self, mock_input):
        expected = 'n'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='s')
    def test_get_user_choice_s(self, mock_input):
        expected = 's'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='w')
    def test_get_user_choice_w(self, mock_input):
        expected = 'w'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='e')
    def test_get_user_choice_e(self, mock_input):
        expected = 'e'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['north', 'n'])
    def test_get_user_choice_wrong(self, mock_input):
        expected = 'n'
        actual = get_user_choice()
        self.assertEqual(expected, actual)
