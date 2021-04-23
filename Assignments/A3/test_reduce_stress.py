from unittest import TestCase
from A3.sud import reduce_stress


class TestReduceStress(TestCase):
    def test_stress_at_20(self):
        my_dict = {'stress': 20}
        reduce_stress(my_character=my_dict)
        expected = 0
        actual = my_dict['stress']
        self.assertEqual(expected, actual)

    def test_stress_at_0(self):
        my_dict = {'stress': 0}
        reduce_stress(my_character=my_dict)
        expected = 0
        actual = my_dict['stress']
        self.assertEqual(expected, actual)

    def test_stress_at_100(self):
        my_dict = {'stress': 100}
        reduce_stress(my_character=my_dict)
        expected = 80
        actual = my_dict['stress']
        self.assertEqual(expected, actual)
