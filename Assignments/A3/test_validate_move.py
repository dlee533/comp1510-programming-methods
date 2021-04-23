from unittest import TestCase
from A3.sud import validate_move


class TestValidateMove(TestCase):
    def test_valid_move(self):
        my_list = [(0, 0)]
        my_dict = {'x': 2, 'y': 2}
        my_str = 'w'
        actual = validate_move(coordinates=my_list, character_coordinates=my_dict, direction=my_str)
        self.assertFalse(actual)

    def test_invalid_move(self):
        my_list = [(2, 3)]
        my_dict = {'x': 2, 'y': 2}
        my_str = 's'
        actual = validate_move(coordinates=my_list, character_coordinates=my_dict, direction=my_str)
        self.assertTrue(actual)