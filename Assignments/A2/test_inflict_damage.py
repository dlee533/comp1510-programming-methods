from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import inflict_damage
import io


class TestInflictDamage(TestCase):
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_inflict_damage_im_dead(self, mock_stdout, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = "Mina died"
        inflict_damage(name, my_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_inflict_damage_my_current_hp(self, mock_stdout, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = "Mina's current HP is 1"
        inflict_damage(name, my_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_inflict_damage_who_killed_me(self, mock_stdout, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = "Amy had successfully attacked"
        inflict_damage(name, my_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=2)
    def test_inflict_damage_attacked_return(self, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = {"Name": "Mina", "Class": "wizard", "HP": [3, 1]}
        actual = inflict_damage(name, my_dictionary)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_inflict_damage_dead_return(self, mock_randint):
        name = "some_name"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = {"Name": "Mina", "Class": "wizard", "HP": [3, 0]}
        actual = inflict_damage(name, my_dictionary)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_inflict_damage_return_equal_hp(self, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = {"Name": "Mina", "Class": "wizard", "HP": [3, 0]}
        actual = inflict_damage(name, my_dictionary)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_inflict_damage_damage_equal_hp_print(self, mock_stdout, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        expected = "Mina died"
        inflict_damage(name, my_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_inflict_damage_less_than_hp_print(self, mock_stdout, mock_randint):
        name = "Amy"
        my_dictionary = {"Name": "Mina", "Class": "wizard", "HP": [3, 3]}
        not_expected = "Mina died"
        inflict_damage(name, my_dictionary)
        self.assertNotIn(not_expected, mock_stdout.getvalue())
