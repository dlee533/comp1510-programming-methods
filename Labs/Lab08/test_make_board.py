from unittest import TestCase
from Lab08.maze import make_board


class TestMakeBoard(TestCase):
    def test_make_board(self):
        expected = {(0, 0): ' 🚶 ', (0, 1): ' o ', (0, 2): ' o ', (0, 3): ' o ', (0, 4): ' o ', (1, 0): ' o ',
                    (1, 1): ' o ', (1, 2): ' o ', (1, 3): ' o ', (1, 4): ' o ', (2, 0): ' o ', (2, 1): ' o ',
                    (2, 2): ' o ', (2, 3): ' o ', (2, 4): ' o ', (3, 0): ' o ', (3, 1): ' o ', (3, 2): ' o ',
                    (3, 3): ' o ', (3, 4): ' o ', (4, 0): ' o ', (4, 1): ' o ', (4, 2): ' o ', (4, 3): ' o ',
                    (4, 4): ' x '}
        actual = make_board()
        self.assertEqual(expected, actual)
