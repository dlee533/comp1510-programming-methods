from unittest import TestCase
from Lab05.lab05 import roll_die
from unittest.mock import patch


class TestRollDie(TestCase):

    def test_roll_die_3neg1(self):
        expected = 0
        actual = roll_die(3, -1)
        self.assertEqual(expected, actual)

    def test_roll_die_neg13(self):
        expected = 0
        actual = roll_die(-1, 3)
        self.assertEqual(expected, actual)

    def test_roll_die_neg10(self):
        expected = 0
        actual = roll_die(-1, 0)
        self.assertEqual(expected, actual)

    def test_roll_die_0neg1(self):
        expected = 0
        actual = roll_die(0, -1)
        self.assertEqual(expected, actual)

    def test_roll_die_00(self):
        expected = 0
        actual = roll_die(0, 0)
        self.assertEqual(expected, actual)

    def test_roll_die_30(self):
        expected = 0 * 3
        actual = roll_die(3, 0)
        self.assertEqual(expected, actual)

    def test_roll_die_03(self):
        expected = 3 * 0
        actual = roll_die(0, 3)
        self.assertEqual(expected, actual)

    def test_roll_die_31(self):
        expected = 1 * 3
        actual = roll_die(3, 1)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_roll_die_33(self, mock_int):
        expected = 3 * 3
        actual = roll_die(3, 6)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=7)
    def test_roll_die_39(self, mock_int):
        expected = 7 * 3
        actual = roll_die(3, 9)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_roll_die_63(self, mock_int):
        expected = 3 * 6
        actual = roll_die(6, 3)
        self.assertEqual(expected, actual)
