from unittest import TestCase
from A3.sud import encounter_instructor
from unittest.mock import patch
import io


class TestEncounterInstructor(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['a', 'flee'])
    def test__invalid_input(self, mock_input, mock_stdout):
        my_dict = {'stress': 0}
        encounter_instructor(my_character=my_dict)
        expected = "Invalid input.\n"
        actual = mock_stdout.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['flee'])
    @patch('random.randint', return_value=2)
    def test_flee_the_scene(self, mock_randint, mock_input, mock_stdout):
        my_dict = {}
        encounter_instructor(my_character=my_dict)
        expected = "you have successfully fled the scene.\n"
        actual = mock_stdout.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['fight'])
    def test_fight_opponent(self, mock_input):
        my_dict = {'name': 'name', 'stress': 0, 'type': 'student', 'credit': 0}
        expected = None
        actual = encounter_instructor(my_character=my_dict)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['surrender'])
    def test_surrender(self, mock_input):
        my_dict = {'name': 'name', 'stress': 0, 'type': 'student', 'credit': 0, 'surrendered': False}
        expected = True
        encounter_instructor(my_character=my_dict)
        actual = my_dict['surrendered']
        self.assertEqual(expected, actual)
