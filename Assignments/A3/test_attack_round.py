from unittest import TestCase
from A3.sud import attack_round
from unittest.mock import patch
import io


class TestAttackRound(TestCase):
    @patch('random.randint', side_effect=[1, 60])
    def test_attack_round_my_credit(self, mock_randint):
        dict_one = {'type': 'student', 'name': 'Mina', 'stress': 50, 'credit': 0}
        dict_two = {'type': 'instructor', 'name': 'Chris', 'stress': 50, 'assignment': 'unittest'}
        attack_round(attacker=dict_one, defender=dict_two)
        self.assertTrue(dict_one['credit'] == 10)

    @patch('random.randint', side_effect=[1, 60])
    def test_attack_round_my_stress(self, mock_randint):
        dict_one = {'type': 'student', 'name': 'Mina', 'stress': 50, 'credit': 0}
        dict_two = {'type': 'instructor', 'name': 'Chris', 'stress': 50, 'assignment': 'unittest'}
        attack_round(attacker=dict_one, defender=dict_two)
        self.assertTrue(dict_one['stress'] == 50)

    @patch('random.randint', side_effect=[1, 60])
    def test_attack_round_instructor_stress(self, mock_randint):
        dict_one = {'type': 'student', 'name': 'Mina', 'stress': 50, 'credit': 0}
        dict_two = {'type': 'instructor', 'name': 'Chris', 'stress': 50, 'assignment': 'unittest'}
        attack_round(attacker=dict_one, defender=dict_two)
        self.assertTrue(dict_two['stress'] == 110)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2, 1, 60, 1, 60])
    def test_attack_round_attack_failed(self, mock_randint, mock_stdout):
        dict_one = {'type': 'student', 'name': 'Mina', 'stress': 50, 'credit': 0}
        dict_two = {'type': 'instructor', 'name': 'Chris', 'stress': 50, 'assignment': 'unittest'}
        attack_round(attacker=dict_one, defender= dict_two)
        expected = "Mina's attack failed."
        actual = mock_stdout.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2, 1, 60, 1, 60])
    def test_attack_round_instructor_attack_points(self, mock_randint, mock_stdout):
        dict_one = {'type': 'student', 'name': 'Mina', 'stress': 50, 'credit': 0}
        dict_two = {'type': 'instructor', 'name': 'Chris', 'stress': 50, 'assignment': 'unittest'}
        attack_round(attacker=dict_one, defender=dict_two)
        expected = "60 points."
        actual = mock_stdout.getvalue()
        self.assertIn(expected, actual)

    def test_attack_round_type_returned(self):
        dict_one = {'type': 'student', 'name': 'Mina', 'stress': 50, 'credit': 0}
        dict_two = {'type': 'instructor', 'name': 'Chris', 'stress': 50, 'assignment': 'unittest'}
        expected = None
        actual = attack_round(attacker=dict_one, defender=dict_two)
        self.assertEqual(expected, actual)