from unittest import TestCase
from A3.sud import game_guide
from unittest.mock import patch
import io


class TestGameGuide(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_guide(self, mock_stdout):
        game_guide()
        expected = ('- w/a/s/d for direction\n'
                    '- help/h/guide for this screen\n'
                    '- map/m for viewing map\n'
                    '- stat/character for viewing statistics\n'
                    '- surrender/quit/q to surrender\n')
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
