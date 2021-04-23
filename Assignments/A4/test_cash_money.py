from unittest import TestCase
from A4.question_5 import cash_money
from unittest.mock import patch
import io


class TestCashMoney(TestCase):
    def test_cash_money_zero(self):
        expected = {}
        actual = cash_money(0)
        self.assertEqual(expected, actual)

    def test_cash_money_one_cent(self):
        expected = {0.01: 1}
        actual = cash_money(0.01)
        self.assertEqual(expected, actual)

    def test_cash_money_one(self):
        expected = {1: 1}
        actual = cash_money(1)
        self.assertEqual(expected, actual)

    def test_cash_money_twenty(self):
        expected = {20: 1}
        actual = cash_money(20)
        self.assertEqual(expected, actual)

    def test_cash_money_hundred(self):
        expected = {100: 1}
        actual = cash_money(100)
        self.assertEqual(expected, actual)

    def test_cash_money_combination(self):
        expected = {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 1}
        actual = cash_money(188.41)
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_cash_money_value_error(self, mock_stderr):
        expected = "Error: the value must be a positive floating point\n"
        cash_money(-5)
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_cash_money_type_error(self, mock_stderr):
        expected = "Error: the value must be a positive floating point\n"
        cash_money("hi")
        actual = mock_stderr.getvalue()
        self.assertEqual(expected, actual)

    def test_cash_money_value_error_returned(self):
        expected = None
        actual = cash_money(-5)
        self.assertEqual(expected, actual)

    def test_cash_money_type_error_returned(self):
        expected = None
        actual = cash_money("hi")
        self.assertEqual(expected, actual)
