from unittest import TestCase
from A4.question_2 import gcd
from unittest.mock import patch
import io


class TestGcd(TestCase):
    def test_gcd_two_zero(self):
        expected = None
        actual = gcd(0, 0)
        self.assertEqual(expected, actual)

    def test_gcd_two_zero_error(self):
        expected = None
        actual = gcd(0, 0)
        self.assertEqual(expected, actual)

    def test_gcd_first_zero(self):
        expected = None
        actual = gcd(0, 1)
        self.assertEqual(expected, actual)

    def test_gcd_second_zero(self):
        expected = None
        actual = gcd(1, 0)
        self.assertEqual(expected, actual)

    def test_gcd_one_call(self):
        expected = 2
        actual = gcd(4, 2)
        self.assertEqual(expected, actual)

    def test_gcd_two_call(self):
        expected = 3
        actual = gcd(9, 6)
        self.assertEqual(expected, actual)

    def test_gcd_one_decimal(self):
        expected = 5
        actual = gcd(-25, 10)
        self.assertEqual(expected, actual)

    def test_gcd_two_decimal(self):
        expected = 5
        actual = gcd(-25, -10)
        self.assertEqual(expected, actual)

    def test_gcd_same_num_positive(self):
        expected = 5
        actual = gcd(5, 5)
        self.assertEqual(expected, actual)

    def test_gcd_same_num_negative(self):
        expected = 5
        actual = gcd(-5, -5)
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_gcd_value_error(self, mock_stderr):
        expected = "Error: a and b must be non zero\n"
        gcd(0, 0)
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_gcd_type_error(self, mock_stderr):
        expected = "Error: a and b must be integers\n"
        gcd(3.5, 5.87)
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)
