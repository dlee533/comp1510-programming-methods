from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import display_without_number
import io


class TestDisplayWithoutNumber(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_without_number_empty_dict(self, mock_stdout):
        list_or_dict = []
        expected = ""
        display_without_number(list_or_dict)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_without_number_int(self, mock_stdout):
        list_or_dict = [1, 2]
        expected = ("- 1\n"
                    "- 2\n")
        display_without_number(list_or_dict)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_without_number_float(self, mock_stdout):
        list_or_dict = [1.0, 2.0]
        expected = ("- 1.0\n"
                    "- 2.0\n")
        display_without_number(list_or_dict)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_without_number_string(self, mock_stdout):
        list_or_dict = ["one", "two"]
        expected = ("- one\n"
                    "- two\n")
        display_without_number(list_or_dict)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_without_number_mixed(self, mock_stdout):
        list_or_dict = [1, 2.0, "three"]
        expected = ("- 1\n"
                    "- 2.0\n"
                    "- three\n")
        display_without_number(list_or_dict)
        self.assertEqual(expected, mock_stdout.getvalue())
