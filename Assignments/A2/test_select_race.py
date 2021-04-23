from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_race
import io


class TestSelectRace(TestCase):
    @patch('builtins.input', side_effect=['dragonborn'])
    def test_select_race_select_one(self, mock_input):
        expected = 'Dragonborn'
        actual = select_race()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['dsaf', 'dragonborn'])
    def test_select_class_select_wrong_then_one(self, mock_input):
        expected = 'Dragonborn'
        actual = select_race()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['dsaf', 'dragonborn'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_race_select_wrong_then_one_print(self, mock_stdout, mock_input):
        expected = "Invalid input."
        select_race()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['dragonborn'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_race_select_one_print(self, mock_stdout, mock_input):
        not_expected = "Invalid input."
        select_race()
        self.assertNotIn(not_expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['dragonborn'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_race_options_print_one(self, mock_stdout, mock_input):
        expected = "- dragonborn"
        select_race()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['dragonborn'])
    def test_select_race_options_print_two(self, mock_input, mock_stdout):
        expected = "- tortle"
        select_race()
        self.assertIn(expected, mock_stdout.getvalue())
