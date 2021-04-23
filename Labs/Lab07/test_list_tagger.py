from unittest import TestCase
from Lab07.midterm import list_tagger


class TestListTagger(TestCase):
    def test_list_tagger_empty_list(self):
        expected = [0]
        actual = list_tagger([])
        self.assertEqual(expected, actual)

    def test_list_tagger_one_element(self):
        expected = [1, 1]
        actual = list_tagger([1])
        self.assertEqual(expected, actual)

    def test_list_tagger_longer_list(self):
        expected = [3, 1, 2, 3]
        actual = list_tagger([1, 2, 3])
        self.assertEqual(expected, actual)
