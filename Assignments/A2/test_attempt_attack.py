from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import attempt_attack
import io


class TestAttemptAttack(TestCase):
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_fail_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [5, 5], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Attack failed"
        attempt_attack(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=-1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_fail_two(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [13, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Attack failed"
        attempt_attack(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=100)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_success_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [5, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        not_expected = "Attack failed"
        attempt_attack(char_one, char_two)
        self.assertNotIn(not_expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=14)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_success_two(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [8, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        not_expected = "Attack failed"
        attempt_attack(char_one, char_two)
        self.assertNotIn(not_expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=13)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_same_return_as_hp_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [130, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Attack failed"
        attempt_attack(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_same_return_as_hp_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [3, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Attack failed"
        attempt_attack(char_two, char_one)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_whose_turn_one(self, mock_stdout):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [3, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Mina's turn to attack..."
        attempt_attack(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_attack_whose_turn_two(self, mock_stdout):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [3, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Amy's turn to attack..."
        attempt_attack(char_two, char_one)
        self.assertIn(expected, mock_stdout.getvalue())
