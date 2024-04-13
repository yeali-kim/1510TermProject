from unittest import TestCase
from unittest.mock import patch
from npc import heca


class TestHeca(TestCase):
    @patch('builtins.input', side_effect=["y", "y"])
    def test_heca(self, _):
        character = {"shawn_quest": True, "heca_found": False}
        heca(character)
        expected = {"shawn_quest": True, "heca_found": True}
        self.assertEqual(expected, character)
