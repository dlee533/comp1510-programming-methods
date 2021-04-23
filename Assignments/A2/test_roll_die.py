from unittest import TestCase
from A2.dungeonsanddragons import roll_die
from unittest.mock import patch


class TestRollDie(TestCase):

    def test_roll_die_negative(self):
        expected = 0
        actual = roll_die(-1, -1)
        self.assertEqual(expected, actual)

    def test_roll_die_negative_roll_zero_side(self):
        expected = 0
        actual = roll_die(-1, 0)
        self.assertEqual(expected, actual)

    def test_roll_die_zero_roll_negative_side(self):
        expected = 0
        actual = roll_die(0, -1)
        self.assertEqual(expected, actual)

    def test_roll_die_negative_roll_positive_side(self):
        expected = 0
        actual = roll_die(-1, 6)
        self.assertEqual(expected, actual)

    def test_roll_die_positive_roll_negative_side(self):
        expected = 0
        actual = roll_die(3, -1)
        self.assertEqual(expected, actual)

    def test_roll_die_zero(self):
        expected = 0
        actual = roll_die(0, 0)
        self.assertEqual(expected, actual)

    def test_roll_die_zero_roll(self):
        expected = 0
        actual = roll_die(0, 6)
        self.assertEqual(expected, actual)

    def test_roll_die_zero_side(self):
        expected = 0
        actual = roll_die(1, 0)
        self.assertEqual(expected, actual)

    def test_roll_die_one(self):
        expected = 1
        actual = roll_die(1, 1)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_roll_die_one_roll(self, mock_randint):
        expected = 3
        actual = roll_die(1, 6)
        self.assertEqual(expected, actual)

    def test_roll_die_one_side(self):
        expected = 3
        actual = roll_die(3, 1)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_roll_die_greater_side(self, mock_randint):
        expected = 9
        actual = roll_die(3, 6)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_roll_die_greater_roll(self, mock_randint):
        expected = 12
        actual = roll_die(6, 2)
        self.assertEqual(expected, actual)
