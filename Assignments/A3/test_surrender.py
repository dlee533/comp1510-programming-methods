from unittest import TestCase
from A3.character import surrender


class TestSurrender(TestCase):
    def test_surrender(self):
        my_dict = {'surrendered': False}
        surrender(character=my_dict)
        expected = True
        actual = my_dict['surrendered']
        self.assertEqual(expected, actual)

