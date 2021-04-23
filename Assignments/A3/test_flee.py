from unittest import TestCase
from A3.character import flee
from unittest.mock import patch
import io


class TestFlee(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=2)
    def test_successfully_fled(self, mock_randint, mock_stdout):
        my_dict = {}
        flee(character_stat=my_dict)
        expected = 'you have successfully fled the scene.\n'
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[1, 50])
    def test_attack_in_the_back(self, mock_randint, mock_stdout):
        my_dict = {'stress': 0}
        flee(character_stat=my_dict)
        expected = 'Instructor had attacked you in the back by 50 points.\n'
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50])
    def test_stress_when_attacked(self, mock_randint):
        my_dict = {'stress': 0}
        flee(character_stat=my_dict)
        expected = 50
        actual = my_dict['stress']
        self.assertEqual(expected, actual)
