from unittest import TestCase
from A3.sud import change_coordinate


class TestChangeCoordinate(TestCase):
    def test_move_up(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 'w'
        change_coordinate(character_coordinates=my_dict, direction=my_str)
        expected = {'x': 2, 'y': 1}
        actual = my_dict
        self.assertEqual(expected, actual)

    def test_move_left(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 'a'
        change_coordinate(character_coordinates=my_dict, direction=my_str)
        expected = {'x': 1, 'y': 2}
        actual = my_dict
        self.assertEqual(expected, actual)

    def test_move_down(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 's'
        change_coordinate(character_coordinates=my_dict, direction=my_str)
        expected = {'x': 2, 'y': 3}
        actual = my_dict
        self.assertEqual(expected, actual)

    def test_move_right(self):
        my_dict = {'x': 2, 'y': 2}
        my_str = 'd'
        change_coordinate(character_coordinates=my_dict, direction=my_str)
        expected = {'x': 3, 'y': 2}
        actual = my_dict
        self.assertEqual(expected, actual)
