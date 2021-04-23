from unittest import TestCase
from A3.sud import attack_succeeded
from unittest.mock import patch


class TestAttackSucceeded(TestCase):
    @patch('random.randint', return_value=1)
    def test_attack_succeeded_true(self, mock_randint):
        expected = True
        actual = attack_succeeded()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_attack_succeeded_false(self, mock_randint):
        expected = False
        actual = attack_succeeded()
        self.assertEqual(expected, actual)
