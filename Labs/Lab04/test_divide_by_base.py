from unittest import TestCase
from Lab04.roman_numbers import divide_by_base


class TestDivide_by_base(TestCase):

    def test_divide_by_base_I(self):
        expected_value = ('I', 0)
        actual_value = divide_by_base(1, 1, '', 'I')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_IV(self):
        expected_value = ('IV', 0)
        actual_value = divide_by_base(4, 4, '', 'IV')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_V(self):
        expected_value = ('V', 0)
        actual_value = divide_by_base(5, 5, '', 'V')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_IX(self):
        expected_value = ('IX', 0)
        actual_value = divide_by_base(9, 9, '', 'IX')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_X(self):
        expected_value = ('X', 0)
        actual_value = divide_by_base(10, 10, '', 'X')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_XL(self):
        expected_value = ('XL', 0)
        actual_value = divide_by_base(40, 40, '', 'XL')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_L(self):
        expected_value = ('L', 0)
        actual_value = divide_by_base(50, 50, '', 'L')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_XC(self):
        expected_value = ('XC', 0)
        actual_value = divide_by_base(90, 90, '', 'XC')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_C(self):
        expected_value = ('C', 0)
        actual_value = divide_by_base(100, 100, '', 'C')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_CD(self):
        expected_value = ('CD', 0)
        actual_value = divide_by_base(400, 400, '', 'CD')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_D(self):
        expected_value = ('D', 0)
        actual_value = divide_by_base(500, 500, '', 'D')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_CM(self):
        expected_value = ('CM', 0)
        actual_value = divide_by_base(900, 900, '', 'CM')
        self.assertEqual(expected_value, actual_value)

    def test_divide_by_base_M(self):
        expected_value = ('M', 0)
        actual_value = divide_by_base(1000, 1000, '', 'M')
        self.assertEqual(expected_value, actual_value)
