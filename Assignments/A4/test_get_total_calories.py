from unittest import TestCase
from A4.question_7 import get_total_calories


class TestGetTotalCalories(TestCase):
    def test_get_total_calories_empty_dict(self):
        expected = 0
        actual = get_total_calories({})
        self.assertEqual(expected, actual)

    def test_get_total_calories_one_item(self):
        expected = 300
        actual = get_total_calories({'a': 300})
        self.assertEqual(expected, actual)

    def test_get_total_calories_two_item(self):
        expected = 600
        actual = get_total_calories({'a': 300, 'b': 300})
        self.assertEqual(expected, actual)

    def test_get_total_calories_three_items(self):
        expected = 1000
        actual = get_total_calories({'a': 300, 'b': 300, 'c': 400})
        self.assertEqual(expected, actual)
