from unittest import TestCase
from A4.question_4 import check_list_length
from unittest.mock import patch
import io


class TestCheckListLength(TestCase):
    @patch('sys.stderr', new_callable=io.StringIO)
    def test_check_list_length_value_err_print(self, mock_stderr):
        expected = "Error: the list cannot be empty\n"
        check_list_length([])
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    def test_check_list_length_value_err(self):
        expected = None
        actual = check_list_length([])
        self.assertEqual(expected, actual)

    def test_check_list_length_non_empty(self):
        expected = None
        actual = check_list_length([1, 2, 3])
        self.assertEqual(expected, actual)
