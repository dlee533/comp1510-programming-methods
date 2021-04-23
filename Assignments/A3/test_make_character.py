from unittest import TestCase
from A3.character import make_character
from unittest.mock import patch


class TestMakeCharacter(TestCase):
    @patch('builtins.input', return_value='Mina')
    def test_make_character(self, mock_input):
        expected = {'name': 'Mina', 'type': 'student', 'x': 2, 'y': 2, 'credit': 0, 'stress': 0, 'iq': 100,
                    'surrendered': False}
        actual = make_character()
        self.assertEqual(expected, actual)
