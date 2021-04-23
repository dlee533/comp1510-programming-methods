from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import print_character
import io


class TestPrintCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_empty_dict(self, mock_stdout):
        character_dictionary = {}
        expected = "Character Details"
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_name_only(self, mock_stdout):
        character_dictionary = {"Name": "Mina"}
        expected = "Name : Mina"
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_strength_only(self, mock_stdout):
        character_dictionary = {"Strength": 3}
        expected = "Strength : 3"
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_empty_inventory_only(self, mock_stdout):
        character_dictionary = {"Inventory": []}
        expected = "Inventory :"
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_inventory_only(self, mock_stdout):
        character_dictionary = {"Inventory": ["Sword", "Dagger"]}
        expected = "Inventory : <Sword> <Dagger>"
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hp_only(self, mock_stdout):
        character_dictionary = {"HP": [1, 1]}
        expected = "HP : 1/1"
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_inventory_hp(self, mock_stdout):
        character_dictionary = {"Inventory": ["Sword", "Dagger"], "HP": [1, 1]}
        expected = ("Inventory : <Sword> <Dagger>\n"
                    "HP : 1/1\n")
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_name_hp(self, mock_stdout):
        character_dictionary = {"Name": "Mina", "HP": [1, 1]}
        expected = ("Name : Mina\n"
                    "HP : 1/1\n")
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_two_attribute(self, mock_stdout):
        character_dictionary = {"Name": "Mina", "Constitution": 5}
        expected = ("Name : Mina\n"
                    "Constitution : 5\n")
        print_character(character_dictionary)
        self.assertIn(expected, mock_stdout.getvalue())
