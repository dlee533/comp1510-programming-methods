from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import combat_round
import io


class TestCombatRound(TestCase):
    def test_combat_round_return(self):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [3, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = None
        actual = combat_round(char_one, char_two)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 3, 5, 7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_failed_attack_both(self, mock_stdout, mock_randint):
        char_one = {'Name': 'Duqiya', 'Race': 'Verdan', 'Class': 'wizard', 'HP': [2, 2], 'Strength': 5, 'Dexterity': 8,
                    'Constitution': 7, 'Intelligence': 7, 'Wisdom': 9, 'Charisma': 12, 'XP': 0, 'Inventory': []}
        char_two = {'Name': 'Hevo', 'Race': 'Gith', 'Class': 'warlock', 'HP': [8, 8], 'Strength': 7, 'Dexterity': 10,
                    'Constitution': 13, 'Intelligence': 14, 'Wisdom': 10, 'Charisma': 11, 'XP': 0, 'Inventory': []}
        expected = ("Hevo's turn to attack...\n"
                    "Attack failed.\n"
                    "Duqiya's turn to attack...\n"
                    "Attack failed.\n")
        combat_round(char_one, char_two)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[1, 3, 15, 5, 8])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_failed_attack_one(self, mock_stdout, mock_randint):
        char_one = {'Name': 'Duqiya', 'Race': 'Verdan', 'Class': 'wizard', 'HP': [6, 6], 'Strength': 5, 'Dexterity': 8,
                    'Constitution': 7, 'Intelligence': 7, 'Wisdom': 19, 'Charisma': 12, 'XP': 0, 'Inventory': []}
        char_two = {'Name': 'Hevo', 'Race': 'Gith', 'Class': 'warlock', 'HP': [8, 8], 'Strength': 7, 'Dexterity': 10,
                    'Constitution': 13, 'Intelligence': 14, 'Wisdom': 10, 'Charisma': 11, 'XP': 0, 'Inventory': []}
        expected = ("Hevo's turn to attack...\n"
                    "Hevo had successfully attacked Duqiya by 5 HP.\n"
                    "Duqiya's current HP is 1.\n"
                    "Duqiya's turn to attack...\n"
                    "Attack failed.\n")
        combat_round(char_one, char_two)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[1, 3, 5, 20, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_failed_attack_two(self, mock_stdout, mock_randint):
        char_one = {'Name': 'Duqiya', 'Race': 'Verdan', 'Class': 'wizard', 'HP': [6, 6], 'Strength': 5, 'Dexterity': 8,
                    'Constitution': 7, 'Intelligence': 7, 'Wisdom': 8, 'Charisma': 12, 'XP': 0, 'Inventory': []}
        char_two = {'Name': 'Hevo', 'Race': 'Gith', 'Class': 'warlock', 'HP': [8, 8], 'Strength': 7, 'Dexterity': 10,
                    'Constitution': 13, 'Intelligence': 14, 'Wisdom': 10, 'Charisma': 11, 'XP': 0, 'Inventory': []}
        expected = ("Hevo's turn to attack...\n"
                    "Attack failed.\n"
                    "Duqiya's turn to attack...\n"
                    "Duqiya had successfully attacked Hevo by 10 HP.\n"
                    "Hevo died.\n")
        combat_round(char_one, char_two)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[1, 3, 2, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_both_attack_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Dongmin", "Class": "wizard", "HP": [3, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Amy's turn to attack..."
        combat_round(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[1, 3, 2, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_both_attack_two(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [3, 3], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Mina's turn to attack..."
        combat_round(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[1, 3, 5, 7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_died_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [2, 2], "Dexterity": 2}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Mina died."
        combat_round(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[3, 1, 12, 17, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_died_two(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [2, 2], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 11}
        expected = "Amy died."
        combat_round(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[3, 1, 14, 3, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_hp_changes_one(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [2, 2], "Dexterity": 13}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Mina had successfully attacked Amy by 3 HP."
        combat_round(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', side_effect=[1, 3, 14, 3, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_hp_changes_two(self, mock_stdout, mock_randint):
        char_one = {"Name": "Mina", "Class": "wizard", "HP": [2, 2], "Dexterity": 3}
        char_two = {"Name": "Amy", "Class": "ranger", "HP": [13, 13], "Dexterity": 13}
        expected = "Amy had successfully attacked Mina by 3 HP."
        combat_round(char_one, char_two)
        self.assertIn(expected, mock_stdout.getvalue())
