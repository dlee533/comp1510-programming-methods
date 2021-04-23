from unittest import TestCase
from A3.character import print_character
from unittest.mock import patch
import io


class TestPrintCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_pair(self, mock_output):
        my_dict = {'Name': 'Mina'}
        print_character(character=my_dict)
        expected = (
            "----------------------------\n"
            "Name: Mina\n"
            "----------------------------\n"
        )
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_pairs(self, mock_output):
        my_dict = {'Name': 'Mina', 'School': 'BCIT', 'Program': 'CST'}
        print_character(character=my_dict)
        expected = (
            "----------------------------\n"
            "Name: Mina\n"
            "School: BCIT\n"
            "Program: CST\n"
            "----------------------------\n"
        )
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
