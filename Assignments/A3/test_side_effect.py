from unittest import TestCase
from A3.sud import side_effect
from unittest.mock import patch


class TestSideEffect(TestCase):
    @patch('random.randint', return_value=2)
    def test_stress_at_20(self, mock_randint):
        my_dict = {'stress': 20}
        side_effect(character_info=my_dict)
        expected = 0
        actual = my_dict['stress']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_stress_at_0(self, mock_randint):
        my_dict = {'stress': 0}
        side_effect(character_info=my_dict)
        expected = 0
        actual = my_dict['stress']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_stress_at_100(self, mock_randint):
        my_dict = {'stress': 100}
        side_effect(character_info=my_dict)
        expected = 80
        actual = my_dict['stress']
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='surrender')
    @patch('random.randint', return_value=1)
    def test_surrendered(self, mock_randint, mock_input):
        my_dict = {'stress': 100, 'surrendered': False}
        side_effect(character_info=my_dict)
        expected = True
        actual = my_dict['surrendered']
        self.assertEqual(expected, actual)
