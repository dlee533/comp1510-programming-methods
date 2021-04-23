from unittest import TestCase
from A4.question_3 import dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra_empty_list(self):
        my_list = []
        dijkstra(colour_list=my_list)
        expected = []
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_list_length_one(self):
        my_list = ['red']
        dijkstra(colour_list=my_list)
        expected = ['red']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_only_red(self):
        my_list = ['red', 'red', 'red']
        dijkstra(colour_list=my_list)
        expected = ['red', 'red', 'red']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_only_blue(self):
        my_list = ['blue', 'blue', 'blue']
        dijkstra(colour_list=my_list)
        expected = ['blue', 'blue', 'blue']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_only_white(self):
        my_list = ['white', 'white', 'white']
        dijkstra(colour_list=my_list)
        expected = ['white', 'white', 'white']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_red_white(self):
        my_list = ['white', 'red']
        dijkstra(colour_list=my_list)
        expected = ['red', 'white']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_red_blue(self):
        my_list = ['blue', 'red']
        dijkstra(colour_list=my_list)
        expected = ['red', 'blue']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_blue_white(self):
        my_list = ['blue', 'white']
        dijkstra(colour_list=my_list)
        expected = ['white', 'blue']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_all_colours_one_of_each(self):
        my_list = ['blue', 'white', 'red']
        dijkstra(colour_list=my_list)
        expected = ['red', 'white', 'blue']
        actual = my_list
        self.assertEqual(expected, actual)

    def test_dijkstra_all_colours_random_numbers(self):
        my_list = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
        dijkstra(colour_list=my_list)
        expected = ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
        actual = my_list
        self.assertEqual(expected, actual)
