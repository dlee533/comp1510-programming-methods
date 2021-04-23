from unittest import TestCase
from Lab08.maze import get_new_coordinate


class TestGetNewCoordinate(TestCase):
    def test_get_new_coordinate_north(self):
        coor_dict = {"x": 0, "y": 0}
        direction = 'n'
        expected = (0, -1)
        actual = get_new_coordinate(coor_dict, direction)
        self.assertEqual(expected, actual)

    def test_get_new_coordinate_south(self):
        coor_dict = {"x": 0, "y": 0}
        direction = 's'
        expected = (0, 1)
        actual = get_new_coordinate(coor_dict, direction)
        self.assertEqual(expected, actual)

    def test_get_new_coordinate_west(self):
        coor_dict = {"x": 0, "y": 0}
        direction = 'w'
        expected = (-1, 0)
        actual = get_new_coordinate(coor_dict, direction)
        self.assertEqual(expected, actual)

    def test_get_new_coordinate_east(self):
        coor_dict = {"x": 0, "y": 0}
        direction = 'e'
        expected = (1, 0)
        actual = get_new_coordinate(coor_dict, direction)
        self.assertEqual(expected, actual)
