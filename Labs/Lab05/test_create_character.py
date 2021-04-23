from unittest import TestCase
from Lab05.lab05 import create_character
from unittest.mock import patch


class TestCreateCharacter(TestCase):

    @patch('random.choice', side_effect=["c", "i"])
    @patch('random.randint', return_value=3)
    def test_create_character_one_syllable(self, mock_num, mock_choice):
        expected = ["Ci", ["Strength", 9], ["Dexterity", 9], ["Constitution",
                    9], ["Intelligence", 9], ["Wisdom", 9], ["Charisma", 9]]
        actual = create_character(1)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_create_character_zero_syllable(self, mock_num):
        expected = ["", ["Strength", 9], ["Dexterity", 9], ["Constitution",
                    9], ["Intelligence", 9], ["Wisdom", 9], ["Charisma", 9]]
        actual = create_character(0)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_create_character_negative_syllable(self, mock_num):
        expected = ["", ["Strength", 9], ["Dexterity", 9], ["Constitution",
                    9], ["Intelligence", 9], ["Wisdom", 9], ["Charisma", 9]]
        actual = create_character(-1)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["c", "i", "d", "e"])
    @patch('random.randint', return_value=1)
    def test_create_character_roll_1(self, mock_num, mock_choice):
        expected = ["Cide", ["Strength", 3], ["Dexterity", 3], ["Constitution",
                    3], ["Intelligence", 3], ["Wisdom", 3], ["Charisma", 3]]
        actual = create_character(2)
        self.assertEqual(expected, actual)
