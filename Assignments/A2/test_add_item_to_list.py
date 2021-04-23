from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import add_item_to_list
import io


class TestAddItemToList(TestCase):
    @patch('builtins.input', side_effect=['-1'])
    def test_add_item_to_list_select_none_empty_list(self, mock_input):
        my_list = []
        expected = None
        actual = add_item_to_list(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '-1'])
    def test_add_item_to_list_select_empty_list(self, mock_input):
        my_list = []
        expected = None
        actual = add_item_to_list(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_add_item_to_list_select_one(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = 1
        actual = add_item_to_list(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['asdf', '1'])
    def test_add_item_to_list_wrong_input_then_one(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = 1
        actual = add_item_to_list(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['asdf', '-1'])
    def test_add_item_to_list_wrong_input_then_neg_one(self, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = None
        actual = add_item_to_list(my_list)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['asdf', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_item_to_list_wrong_input_then_one(self, mock_stdout, mock_input):
        my_list = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = "Invalid choice."
        add_item_to_list(my_list)
        self.assertIn(expected, mock_stdout.getvalue())