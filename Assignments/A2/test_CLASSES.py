from unittest import TestCase
from A2.dungeonsanddragons import CLASSES


class TestCLASSES(TestCase):
    def test_CLASSES(self):
        expected = {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10,
                    "monk": 8, "paladin": 10, "ranger": 10, "rogue": 8, "sorcerer": 6,
                    "warlock": 8, "wizard": 6}
        actual = CLASSES()
        self.assertEqual(expected, actual)
