from unittest import TestCase
from Lab10.question_2 import gcd


class TestGcd(TestCase):
    def test_gcd_two_zero(self):
        expected = 0
        actual = gcd(0, 0)
        self.assertEqual(expected, actual)

    def test_gcd_first_zero(self):
        expected = 1
        actual = gcd(0, 1)
        self.assertEqual(expected, actual)

    def test_gcd_second_zero(self):
        expected = 1
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