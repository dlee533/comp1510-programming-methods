from unittest import TestCase
from A4.question_7 import print_informations
from unittest.mock import patch
import io


class TestPrintInformations(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_informations_one_item(self, mock_stdout):
        expected = "Food Items: ['mango']"
        print_informations({"mango": 300})
        actual = mock_stdout.getvalue()
        self.assertIn(expected, actual)