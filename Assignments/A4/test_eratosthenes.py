from unittest import TestCase
from A4.question_1 import eratosthenes
from unittest.mock import patch
import io


class TestEratosthenes(TestCase):
    def test_eratosthenes_0(self):
        expected = []
        actual = eratosthenes(0)
        self.assertEqual(expected, actual)

    def test_eratosthenes_1(self):
        expected = []
        actual = eratosthenes(1)
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_eratosthenes_negative_print(self, mock_stderr):
        expected = 'Error: upperbound must be a positive integer\n'
        eratosthenes(-5)
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    def test_eratosthenes_negative_return(self):
        expected = None
        actual = eratosthenes(-5)
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_eratosthenes_float_print(self, mock_stderr):
        expected = "Error: 'float' object cannot be interpreted as an integer\n"
        eratosthenes(1.5)
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    def test_eratosthenes_float_return(self):
        expected = None
        actual = eratosthenes(1.5)
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_eratosthenes_string_print(self, mock_stderr):
        expected = "Error: '<' not supported between instances of 'str' and 'int'\n"
        eratosthenes("hi")
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    def test_eratosthenes_string_return(self):
        expected = None
        actual = eratosthenes("hi")
        self.assertEqual(expected, actual)

    def test_eratosthenes_2(self):
        expected = [2]
        actual = eratosthenes(2)
        self.assertEqual(expected, actual)

    def test_eratosthenes_30(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        actual = eratosthenes(30)
        self.assertEqual(expected, actual)
