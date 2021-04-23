from unittest import TestCase
from A2.dungeonsanddragons import generate_syllable
from unittest.mock import patch


class TestGenerateSyllable(TestCase):

    @patch('random.choice', side_effect=['y', 'y'])
    def test_generate_syllable_yy(self, mock_value):
        expected = 'yy'
        actual = generate_syllable()
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a'])
    def test_generate_syllable_ba(self, mock_value):
        expected = 'ba'
        actual = generate_syllable()
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['z', 'y'])
    def test_generate_syllable_zy(self, mock_value):
        expected = 'zy'
        actual = generate_syllable()
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['g', 'o'])
    def test_generate_syllable_go(self, mock_value):
        expected = 'go'
        actual = generate_syllable()
        self.assertEqual(expected, actual)
