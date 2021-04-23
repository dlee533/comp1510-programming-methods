from unittest import TestCase
from A4.question_8 import im_not_sleepy



class TestImNotSleepy(TestCase):
    def test_im_not_sleepy(self):
        expected = ('10:08', 21)
        actual = im_not_sleepy()
        self.assertEqual(expected, actual)
