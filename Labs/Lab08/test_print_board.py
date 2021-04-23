from unittest import TestCase
from Lab08.maze import print_board
from unittest.mock import patch
import io


class TestPrintBoard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_start(self, mock_stdout):
        board = {(0, 0): ' 🚶 ', (0, 1): ' o ', (0, 2): ' o ', (0, 3): ' o ', (0, 4): ' o ', (1, 0): ' o ',
                 (1, 1): ' o ', (1, 2): ' o ', (1, 3): ' o ', (1, 4): ' o ', (2, 0): ' o ', (2, 1): ' o ',
                 (2, 2): ' o ', (2, 3): ' o ', (2, 4): ' o ', (3, 0): ' o ', (3, 1): ' o ', (3, 2): ' o ',
                 (3, 3): ' o ', (3, 4): ' o ', (4, 0): ' o ', (4, 1): ' o ', (4, 2): ' o ', (4, 3): ' o ',
                 (4, 4): ' x '}
        expected = (" 🚶  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  x \n")
        print_board(board)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_middle(self, mock_stdout):
        board = {(0, 0): ' o ', (0, 1): ' o ', (0, 2): ' o ', (0, 3): ' o ', (0, 4): ' o ', (1, 0): ' o ',
                 (1, 1): ' o ', (1, 2): ' o ', (1, 3): ' o ', (1, 4): ' o ', (2, 0): ' o ', (2, 1): ' o ',
                 (2, 2): ' 🚶 ', (2, 3): ' o ', (2, 4): ' o ', (3, 0): ' o ', (3, 1): ' o ', (3, 2): ' o ',
                 (3, 3): ' o ', (3, 4): ' o ', (4, 0): ' o ', (4, 1): ' o ', (4, 2): ' o ', (4, 3): ' o ',
                 (4, 4): ' x '}
        expected = (" o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  🚶  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  x \n")
        print_board(board)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_end(self, mock_stdout):
        board = {(0, 0): ' o ', (0, 1): ' o ', (0, 2): ' o ', (0, 3): ' o ', (0, 4): ' o ', (1, 0): ' o ',
                 (1, 1): ' o ', (1, 2): ' o ', (1, 3): ' o ', (1, 4): ' o ', (2, 0): ' o ', (2, 1): ' o ',
                 (2, 2): ' o ', (2, 3): ' o ', (2, 4): ' o ', (3, 0): ' o ', (3, 1): ' o ', (3, 2): ' o ',
                 (3, 3): ' o ', (3, 4): ' o ', (4, 0): ' o ', (4, 1): ' o ', (4, 2): ' o ', (4, 3): ' o ',
                 (4, 4): ' 🚶 '}
        expected = (" o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  🚶 \n")
        print_board(board)
        self.assertEqual(expected, mock_stdout.getvalue())
