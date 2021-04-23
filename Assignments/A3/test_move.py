from unittest import TestCase
from A3.sud import move
from unittest.mock import patch
import io


class TestMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_toward_wall(self, mock_stdout):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 0}
        direction = 'w'
        move(board, cha, direction)
        expected = "There's a wall in that direction\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    def test_move_toward_wall_coordinate(self):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 0}
        direction = 'w'
        move(board, cha, direction)
        expected = {'x': 0, 'y': 0}
        actual = cha
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[2])
    def test_stress_reduced_20(self, mock_randint):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 1, 'stress': 20}
        direction = 'w'
        move(board, cha, direction)
        expected = 0
        actual = cha['stress']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[2])
    def test_stress_reduced_0(self, mock_randint):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 1, 'stress': 0}
        direction = 'w'
        move(board, cha, direction)
        expected = 0
        actual = cha['stress']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[2])
    def test_stress_reduced_100(self, mock_randint):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 1, 'stress': 100}
        direction = 'w'
        move(board, cha, direction)
        expected = 80
        actual = cha['stress']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_changed_coordinate(self, mock_randint):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 1, 'stress': 0}
        direction = 'w'
        move(board, cha, direction)
        expected = {'x': 0, 'y': 0, 'stress': 0}
        actual = cha
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[1])
    @patch('random.choice', return_value=['chris'])
    def test_encounter_opponent(self, mock_choice, mock_randint):
        board = [(0, 0)]
        cha = {'x': 0, 'y': 1, 'stress': 0}
        direction = 'w'
        move(board, cha, direction)
        expected = 0
        actual = cha['stress']
        self.assertEqual(expected, actual)

