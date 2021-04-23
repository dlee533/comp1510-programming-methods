from unittest import TestCase
from unittest.mock import patch
from Lab08.maze import game
import io


class TestGame(TestCase):
    @patch('builtins.input', side_effect=['s', 's', 's', 's', 'e', 'e', 'e', 'e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_steps(self, mock_stdout, mock_input):
        expected = "It took you 8 steps to exit."
        game()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['s', 's', 's', 's', 'e', 'e', 'e', 'e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_game_complete(self, mock_stdout, mock_input):
        expected = 'Congratulation! You found the exit.'
        game()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['s', 's', 's', 's', 's', 'e', 'e', 'e', 'e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_game_wall(self, mock_stdout, mock_input):
        expected = "There's a wall in that direction."
        game()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['s', 's', 's', 's', 'n', 's', 'e', 'e', 'e', 'e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_ten_steps(self, mock_stdout, mock_input):
        expected = "It took you 10 steps to exit."
        game()
        self.assertIn(expected, mock_stdout.getvalue())
