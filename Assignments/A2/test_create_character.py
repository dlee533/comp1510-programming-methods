from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import create_character
import io


class TestCreateCharacter(TestCase):
    @patch('builtins.input', side_effect=['barbarian', 'gith'])
    @patch('random.randint', return_value=5)
    def test_create_character_name_len_zero(self, mock_randint, mock_input):
        expected = ""
        actual = create_character(0)['Name']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['barbarian', 'gith'])
    @patch('random.randint', return_value=5)
    def test_create_character_existing_key(self, mock_randint, mock_input):
        expected = ['Name', 'HP', 'Class', 'Race']
        actual = create_character(0)
        self.assertTrue(key in actual for key in expected)

    @patch('builtins.input', side_effect=['barbarian', 'gith'])
    @patch('random.randint', return_value=5)
    def test_create_character_type(self, mock_randint, mock_input):
        expected = dict
        actual = type(create_character(0))
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['adsf', 'barbarian', 'gith'])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_wrong_class(self, mock_stdout, mock_randint, mock_input):
        expected = "Invalid input."
        create_character(0)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['barbarian', 'dasf', 'gith'])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_wrong_race(self, mock_stdout, mock_randint, mock_input):
        expected = "Invalid input."
        create_character(0)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['barbarian', 'gith'])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_not_wrong(self, mock_stdout, mock_randint, mock_input):
        not_expected = "Invalid input."
        create_character(0)
        self.assertNotIn(not_expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['barbarian', 'gith'])
    @patch('random.randint', return_value=5)
    def test_create_character_len_dict(self, mock_randint, mock_input):
        expected = 12
        actual = len(create_character(0))
        self.assertEqual(expected, actual)
