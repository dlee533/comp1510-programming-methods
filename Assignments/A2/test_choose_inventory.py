from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import choose_inventory
import io


class TestChooseInventory(TestCase):
    @patch('builtins.input', side_effect=['-1'])
    def test_choose_inventory_empty_list_no_selection(self, mock_input):
        my_list = []
        expected = []
        actual = choose_inventory(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['-1'])
    def test_choose_inventory_no_selection(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = []
        actual = choose_inventory(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '-1'])
    def test_choose_inventory_empty_list_selection(self, mock_input):
        my_list = []
        expected = []
        actual = choose_inventory(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '-1'])
    def test_choose_inventory_selection(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = ["Acid"]
        actual = choose_inventory(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '2', '3', '-1'])
    def test_choose_inventory_multiple_selection(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = ["Acid", "Arrows", "Battleaxe"]
        actual = choose_inventory(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['asdfa', '-1'])
    def test_choose_inventory_wrong_selection(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = []
        actual = choose_inventory(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['asdfa', '-1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_wrong_selection_print(self, mock_stdout, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = "Invalid choice."
        choose_inventory(my_list)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1', '-1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_wrong_selection_print(self, mock_stdout, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        not_expected = "Invalid choice."
        choose_inventory(my_list)
        self.assertNotIn(not_expected, mock_stdout.getvalue())
