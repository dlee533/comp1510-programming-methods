from unittest import TestCase
from Lab07.midterm import prepender


class TestPrepender(TestCase):
    def test_prepender_empty_list_empty_string(self):
        string_list = []
        expected = []
        prepender(string_list, '')
        self.assertEqual(expected, string_list)

    def test_prepender_empty_list_some_string(self):
        string_list = []
        expected = []
        prepender(string_list, 'Python')
        self.assertEqual(expected, string_list)

    def test_prepender_list_of_one_and_empty_string(self):
        string_list = ["Python"]
        expected = ['Python']
        prepender(string_list, '')
        self.assertEqual(expected, string_list)

    def test_prepender_list_of_one_and_some_string(self):
        string_list = ["Python"]
        expected = ['I love Python']
        prepender(string_list, 'I love ')
        self.assertEqual(expected, string_list)

    def test_prepender_list_of_many_and_empty_string(self):
        string_list = ["Python", "is", "better", "than", "JavaScript"]
        expected = ["Python", "is", "better", "than", "JavaScript"]
        prepender(string_list, '')
        self.assertEqual(expected, string_list)

    def test_prepender_list_of_many_and_some_string(self):
        string_list = ["Python", "is", "better", "than", "JavaScript"]
        expected = ["Umm...Python", "Umm...is", "Umm...better", "Umm...than", "Umm...JavaScript"]
        prepender(string_list, 'Umm...')
        self.assertEqual(expected, string_list)
