from unittest import TestCase
from unittest.mock import patch
import io
from A3.board import print_board


class TestPrintBoard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_middle(self, mock_stdout):
        my_dict = {'x': 2, 'y': 2}
        print_board(character_coordinates=my_dict)
        expected = (" o  o  o  o  o \n" 
                    " o  o  o  o  o \n" 
                    " o  o  🚶  o  o \n" 
                    " o  o  o  o  o \n" 
                    " o  o  o  o  o \n")
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_corner1(self, mock_stdout):
        my_dict = {'x': 0, 'y': 0}
        print_board(character_coordinates=my_dict)
        expected = (" 🚶  o  o  o  o \n" 
                    " o  o  o  o  o \n" 
                    " o  o  o  o  o \n" 
                    " o  o  o  o  o \n" 
                    " o  o  o  o  o \n")
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_corner2(self, mock_stdout):
        my_dict = {'x': 4, 'y': 4}
        print_board(character_coordinates=my_dict)
        expected = (" o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  o \n"
                    " o  o  o  o  🚶 \n")
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
