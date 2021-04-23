from unittest import TestCase
from Lab08.maze import check_if_exit_reached


class TestCheckIfExitReached(TestCase):
    def test_check_if_exit_reached_zero(self):
        my_dict = {'x': 0, 'y': 0}
        actual = check_if_exit_reached(my_dict)
        self.assertFalse(actual)

    def test_check_if_exit_reached_one_neg(self):
        my_dict = {'x': -1, 'y': 0}
        actual = check_if_exit_reached(my_dict)
        self.assertFalse(actual)

    def test_check_if_exit_reached_two_neg(self):
        my_dict = {'x': -1, 'y': -1}
        actual = check_if_exit_reached(my_dict)
        self.assertFalse(actual)

    def test_check_if_exit_reached_one_pos(self):
        my_dict = {'x': 1, 'y': 0}
        actual = check_if_exit_reached(my_dict)
        self.assertFalse(actual)

    def test_check_if_exit_reached_two_pos(self):
        my_dict = {'x': 1, 'y': 1}
        actual = check_if_exit_reached(my_dict)
        self.assertFalse(actual)

    def test_check_if_exit_reached_one_four(self):
        my_dict = {'x': 4, 'y': 0}
        actual = check_if_exit_reached(my_dict)
        self.assertFalse(actual)

    def test_check_if_exit_reached_two_four(self):
        my_dict = {'x': 4, 'y': 4}
        actual = check_if_exit_reached(my_dict)
        self.assertTrue(actual)
