from unittest import TestCase
from unittest.mock import patch
import io
from Lab04.time_calculator import time_calculator


class TestTime_calculator(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_zero(self, mock_stdout):
        seconds = 0
        expected_output = '0 0 0 0\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_second(self, mock_stdout):
        seconds = 1
        expected_output = '0 0 0 1\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_seconds(self, mock_stdout):
        seconds = 30
        expected_output = '0 0 0 30\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_minute(self, mock_stdout):
        seconds = 60
        expected_output = '0 0 1 0\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_minutes(self, mock_stdout):
        seconds = 2019
        expected_output = '0 0 33 39\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_hour(self, mock_stdout):
        seconds = 3600
        expected_output = '0 1 0 0\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_hours(self, mock_stdout):
        seconds = 10000
        expected_output = '0 2 46 40\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_day(self, mock_stdout):
        seconds = 86400
        expected_output = '1 0 0 0\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_more_days(self, mock_stdout):
        seconds = 61000000
        expected_output = '706 0 26 40\n'
        time_calculator(seconds)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
