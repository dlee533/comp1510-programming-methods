from unittest import TestCase
import io
from unittest.mock import patch
from Lab05.lab05 import print_character


class TestPrintCharacter(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        character_list = ["Mina", ["Strength", 100]]
        expected = "Character Stats\nName : Mina\nStrength : 100\n"
        print_character(character_list)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_with_item(self, mock_stdout):
        character_list = ["Mina", ["Strength", 100], ["Items", "Sword", "Gun", "Rock"]]
        expected = "Character Stats\nName : Mina\nStrength : 100\nItems : <Sword> <Gun> <Rock>\n"
        print_character(character_list)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_with_name_only(self, mock_stdout):
        character_list = ["Mina"]
        expected = "Character Stats\nName : Mina\n"
        print_character(character_list)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_with_empty_name(self, mock_stdout):
        character_list = [""]
        expected = "Character Stats\nName : \n"
        print_character(character_list)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_with_item_switched(self, mock_stdout):
        character_list = ["Mina", ["Items", "Sword", "Gun", "Rock"], ["Strength", 100]]
        expected = "Character Stats\nName : Mina\nItems : <Sword> <Gun> <Rock>\nStrength : 100\n"
        print_character(character_list)
        self.assertEqual(expected, mock_stdout.getvalue())
