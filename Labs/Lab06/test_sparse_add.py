from unittest import TestCase
from Lab06.sparsevector import sparse_add


class TestSparseAdd(TestCase):
    def test_sparse_add_empty_dict(self):
        expected = {}
        actual = sparse_add({}, {})
        self.assertEqual(expected, actual)

    def test_sparse_add_empty_dict_one(self):
        expected = {1: 4}
        actual = sparse_add({1: 4}, {})
        self.assertEqual(expected, actual)

    def test_sparse_add_empty_dict_two(self):
        expected = {1: 4}
        actual = sparse_add({}, {1: 4})
        self.assertEqual(expected, actual)

    def test_sparse_add_all_same_indices(self):
        expected = {1: 5, 2: 5}
        actual = sparse_add({1: 4, 2: 2}, {1: 1, 2:3})
        self.assertEqual(expected, actual)

    def test_sparse_add_some_same_indices_one(self):
        expected = {1: 5, 2: 1}
        actual = sparse_add({1: 4}, {1: 1, 2: 1})
        self.assertEqual(expected, actual)

    def test_sparse_add_some_same_indices_two(self):
        expected = {1: 5, 2: 1}
        actual = sparse_add({1: 4, 2: 1}, {1: 1})
        self.assertEqual(expected, actual)

    def test_sparse_add_all_different(self):
        expected = {1: 4, 2: 1, 3: 1, 4: 6}
        actual = sparse_add({1: 4, 3: 1}, {2: 1, 4: 6})
        self.assertEqual(expected, actual)

    def test_sparse_all_zero(self):
        expected = {}
        actual = sparse_add({1: 4, 3: 1}, {1: -4, 3: -1})
        self.assertEqual(expected, actual)

    def test_sparse_some_zero_one(self):
        expected = {1: 4}
        actual = sparse_add({1: 4, 3: 1}, {3: -1})
        self.assertEqual(expected, actual)

    def test_sparse_some_zero_two(self):
        expected = {3: -1}
        actual = sparse_add({1: 4}, {1: -4, 3: -1})
        self.assertEqual(expected, actual)