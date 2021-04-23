from unittest import TestCase
from A3.opponent import create_instructor
from unittest.mock import patch


class TestCreateInstructor(TestCase):
    @patch('random.choice', side_effect=['unittest', 'chris'])
    def test_first_combination(self, mock_choice):
        expected = {'name': 'chris', 'type': 'instructor', 'stress': 50, 'assignment': 'unittest'}
        actual = create_instructor()
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['quiz', 'sam'])
    def test_second_combination(self, mock_choice):
        expected = {'name': 'sam', 'type': 'instructor', 'stress': 50, 'assignment': 'quiz'}
        actual = create_instructor()
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['lab', 'neda'])
    def test_third_combination(self, mock_choice):
        expected = {'name': 'neda', 'type': 'instructor', 'stress': 50, 'assignment': 'lab'}
        actual = create_instructor()
        self.assertEqual(expected, actual)
