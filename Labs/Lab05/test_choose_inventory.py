from unittest import TestCase
from Lab05.lab05 import choose_inventory
import io
from unittest.mock import patch


class TestChooseInventory(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_negative_selection_print(self, mock_output):
        inventory = ['Sword', 'Spear', 'Shield']
        expected = "Error! Selection cannot be a negative number.\n"
        choose_inventory(inventory, -1)
        self.assertEqual(expected, mock_output.getvalue())

    def test_choose_inventory_selection_negative_selection_return(self):
        inventory = ['Sword', 'Spear', 'Shield']
        expected = []
        actual = choose_inventory(inventory, -1)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_empty_inventory_print(self, mock_output):
        inventory = []
        expected = "Error! Inventory is empty.\n"
        choose_inventory(inventory, -1)
        self.assertEqual(expected, mock_output.getvalue())

    def test_choose_inventory_selection_empty_inventory_return(self):
        inventory = []
        output = choose_inventory(inventory, 0)
        self.assertTrue(item in inventory for item in output)

    def test_choose_inventory_selection_same_as_inventory(self):
        inventory = ['Sword', 'Spear', 'Shield']
        output = choose_inventory(inventory, 3)
        self.assertTrue(item in inventory for item in output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_over_inventory_print(self, mock_output):
        inventory = ['Sword', 'Spear', 'Shield']
        expected = "Error! Selection cannot be greater than the length of inventory."
        choose_inventory(inventory, 53)
        self.assertEqual(expected, mock_output.getvalue())

    def test_choose_inventory_selection_over_inventory_return(self):
        inventory = ['Sword', 'Spear', 'Shield']
        output = choose_inventory(inventory, 53)
        self.assertTrue(item in inventory for item in output)

    def test_choose_inventory_2(self):
        inventory = ['Sword', 'Spear', 'Shield']
        output = choose_inventory(inventory, 2)
        self.assertTrue(item in inventory for item in output)

    def test_choose_inventory_selection_1(self):
        inventory = ['Sword', 'Spear', 'Shield']
        output = choose_inventory(inventory, 1)
        self.assertTrue(item in inventory for item in output)

    def test_choose_inventory_0(self):
        inventory = ['Sword', 'Spear', 'Shield']
        expected = []
        actual = choose_inventory(inventory, 0)
        self.assertEqual(expected, actual)
