from unittest import TestCase
from A3.sud import get_changed_coordinate


class TestGetChangedCoordinate(TestCase):
    def test_move_up(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 'w'
        expected = (2, 1)
        actual = get_changed_coordinate(current_coordinate=my_dict, arrow_key=my_str)
        self.assertEqual(expected, actual)

    def test_move_left(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 'a'
        expected = (1, 2)
        actual = get_changed_coordinate(current_coordinate=my_dict, arrow_key=my_str)
        self.assertEqual(expected, actual)

    def test_move_down(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 's'
        expected = (2, 3)
        actual = get_changed_coordinate(current_coordinate=my_dict, arrow_key=my_str)
        self.assertEqual(expected, actual)

    def test_move_right(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 'd'
        expected = (3, 2)
        actual = get_changed_coordinate(current_coordinate=my_dict, arrow_key=my_str)
        self.assertEqual(expected, actual)
