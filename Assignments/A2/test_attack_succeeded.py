from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import attack_succeeded


class TestAttackSucceeded(TestCase):
    def test_attack_succeeded_num_range(self):
        expected = [True, False]
        actual = attack_succeeded(5)
        self.assertTrue(actual in expected)

    def test_attack_succeeded_type(self):
        expected = bool
        actual = type(attack_succeeded(5))
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_attack_succeeded_same_value(self, mock_randint):
        expected = False
        actual = attack_succeeded(5)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=6)
    def test_attack_succeeded_smaller_dex(self, mock_randint):
        expected = True
        actual = attack_succeeded(5)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_attack_succeeded_greater_dex(self, mock_randint):
        expected = False
        actual = attack_succeeded(5)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=20)
    def test_attack_succeeded_large_return(self, mock_randint):
        expected = True
        actual = attack_succeeded(5)
        self.assertEqual(expected, actual)
