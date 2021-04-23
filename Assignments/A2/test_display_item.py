from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import display_item
import io


class TestDisplayItem(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_item_print_empty_list(self, mock_stdout):
        inventory = []
        expected = "Here is what we have for sale:\n"
        display_item(inventory)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_item_print_list(self, mock_stdout):
        inventory = ["Sword", "Dagger"]
        expected = ("Here is what we have for sale:\n"
                    "1. Sword\n"
                    "2. Dagger\n")
        display_item(inventory)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_item_print_larger_list(self, mock_stdout):
        inventory = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
        expected = ("Here is what we have for sale:\n"
                    "1. Acid\n"
                    "2. Arrows\n"
                    "3. Battleaxe\n"
                    "4. Blowgun\n"
                    "5. Book\n"
                    "6. Crossbow\n"
                    "7. Crowbar\n")
        display_item(inventory)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_item_print_integers(self, mock_stdout):
        inventory = [1, 2, 3, 4, 5]
        expected = ("Here is what we have for sale:\n"
                    "1. 1\n"
                    "2. 2\n"
                    "3. 3\n"
                    "4. 4\n"
                    "5. 5\n")
        display_item(inventory)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_item_print_floats(self, mock_stdout):
        inventory = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected = ("Here is what we have for sale:\n"
                    "1. 1.0\n"
                    "2. 2.0\n"
                    "3. 3.0\n"
                    "4. 4.0\n"
                    "5. 5.0\n")
        display_item(inventory)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_item_print_mixed(self, mock_stdout):
        inventory = [1, 2.0, "three"]
        expected = ("Here is what we have for sale:\n"
                    "1. 1\n"
                    "2. 2.0\n"
                    "3. three\n")
        display_item(inventory)
        self.assertEqual(expected, mock_stdout.getvalue())
