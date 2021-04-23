from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import decide_turn


class TestDecideTurn(TestCase):
    @patch('random.randint', side_effect=[1, 3])
    def test_decide_turn_roll_one_greater(self, mock_randint):
        expected = 1
        actual = decide_turn()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3, 1])
    def test_decide_turn_roll_two_greater(self, mock_randint):
        expected = 0
        actual = decide_turn()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 2, 3])
    def test_decide_turn_same_then_diff_one(self, mock_randint):
        expected = 1
        actual = decide_turn()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 3, 2])
    def test_decide_turn_same_then_diff_two(self, mock_randint):
        expected = 0
        actual = decide_turn()
        self.assertEqual(expected, actual)

    def test_decide_turn_type(self):
        expected = int
        actual = type(decide_turn())
        self.assertEqual(expected, actual)

    def test_decide_turn_possible_return(self):
        expected = [0, 1]
        actual = decide_turn()
        self.assertTrue(actual in expected)
