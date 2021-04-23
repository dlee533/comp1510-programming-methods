from unittest import TestCase
from Lab07.midterm import cutoff


class TestCutoff(TestCase):
    def test_cutoff_empty_list_and_zero(self):
        expected = 0
        actual = cutoff([], 0)
        self.assertEqual(expected, actual)

    def test_cutoff_empty_list_and_five(self):
        expected = 0
        actual = cutoff([], 5)
        self.assertEqual(expected, actual)

    def test_cutoff_list_of_one_zero_and_zero(self):
        with self.assertRaises(ZeroDivisionError):
            cutoff([0], 0)

    def test_cutoff_list_of_one_zero_and_five(self):
        expected = 1
        actual = cutoff([0], 5)
        self.assertEqual(expected, actual)

    def test_cutoff_list_of_one_two_and_two(self):
        expected = 1
        actual = cutoff([2], 2)
        self.assertEqual(expected, actual)

    def test_cutoff_list_of_one_two_and_four(self):
        expected = 0
        actual = cutoff([2], 4)
        self.assertEqual(expected, actual)

    def test_cutoff_list_of_five_positive_and_zero(self):  # ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            cutoff([1, 2, 3, 4, 5], 0)

    def test_cutoff_list_of_five_positive_and_some_divisible(self):
        expected = 2
        actual = cutoff([1, 2, 3, 4, 5], 2)
        self.assertEqual(expected, actual)

    def test_cutoff_list_of_five_positive_and_all_divisible(self):
        expected = 5
        actual = cutoff([2, 2, 2, 2, 2], 2)
        self.assertEqual(expected, actual)

    def test_cutoff_list_of_five_positive_and_not_divisible(self):
        expected = 0
        actual = cutoff([2, 2, 2, 2, 2], 10)
        self.assertEqual(expected, actual)

    def test_cutoff_another_list_of_five_positive_and_all_divisible(self):
        expected = 5
        actual = cutoff([3, 6, 9, 12, 15], 3)
        self.assertEqual(expected, actual)
