from unittest import TestCase
from A4.question_4 import selection_sort
from unittest.mock import patch
import io


class TestSelectionSort(TestCase):
    @patch('sys.stderr', new_callable=io.StringIO)
    def test_selection_sort_type_error(self, mock_stderr):
        expected = "Error: '<' not supported between instances of 'str' and 'float'\n"
        selection_sort([3.5, 'a'])
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_selection_sort_value_error(self, mock_stderr):
        expected = "Error: the list cannot be empty\n"
        selection_sort([])
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    def test_selection_sort_int(self):
        expected = [1, 2, 3]
        actual = selection_sort([3, 2, 1])
        self.assertEqual(expected, actual)

    def test_selection_sort_float(self):
        expected = [1.0, 2.0, 3.0]
        actual = selection_sort([3.0, 2.0, 1.0])
        self.assertEqual(expected, actual)

    def test_selection_sort_int_and_float(self):
        expected = [1, 2, 3.0]
        actual = selection_sort([3.0, 2, 1])
        self.assertEqual(expected, actual)

    def test_selection_sort_str(self):
        expected = ['a', 'b', 'c']
        actual = selection_sort(['c', 'a', 'b'])
        self.assertEqual(expected, actual)