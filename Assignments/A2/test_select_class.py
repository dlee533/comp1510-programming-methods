from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_class
import io


class TestSelectClass(TestCase):
    @patch('builtins.input', side_effect=['barbarian'])
    def test_select_class_select_one(self, mock_input):
        expected = ('barbarian', 12)
        actual = select_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['dsaf', 'barbarian'])
    def test_select_class_select_wrong_then_one(self, mock_input):
        expected = ('barbarian', 12)
        actual = select_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['dsaf', 'barbarian'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_class_select_wrong_then_one_print(self, mock_stdout, mock_input):
        expected = "Invalid input."
        select_class()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['barbarian'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_class_select_one_print(self, mock_stdout, mock_input):
        not_expected = "Invalid input."
        select_class()
        self.assertNotIn(not_expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['barbarian'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_class_options_print_one(self, mock_stdout, mock_input):
        expected = "- barbarian"
        select_class()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['barbarian'])
    def test_select_class_options_print_two(self, mock_input, mock_stdout):
        expected = "- fighter"
        select_class()
        self.assertIn(expected, mock_stdout.getvalue())
