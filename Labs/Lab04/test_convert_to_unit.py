from unittest import TestCase
from Lab04.time_calculator import convert_to_unit


class TestConvert_to_unit(TestCase):

    def test_convert_to_unit_0(self):
        self.assertEqual((0, 0), convert_to_unit(0, 60))

    def test_convert_to_unit_1(self):
        self.assertEqual((1, 0), convert_to_unit(1, 1))

    def test_convert_to_unit_large_num(self):
        self.assertEqual((8, 20), convert_to_unit(500, 60))
