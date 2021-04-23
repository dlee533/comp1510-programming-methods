from unittest import TestCase
from unittest.mock import patch
from A3.sud import decide_turn


class TestDecideTurn(TestCase):
    @patch('random.randint', side_effect=[1, 2])
    def test_instructors_turn(self, mock_randint):
        expected = 'instructor'
        actual = decide_turn()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2, 1])
    def test_students_turn(self, mock_randint):
        expected = 'student'
        actual = decide_turn()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 1, 2])
    def test_instructors_turn_after_tie(self, mock_randint):
        expected = 'instructor'
        actual = decide_turn()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 2, 1])
    def test_students_turn_after_tie(self, mock_randint):
        expected = 'student'
        actual = decide_turn()
        self.assertEqual(expected, actual)
