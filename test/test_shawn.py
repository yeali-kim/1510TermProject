from unittest import TestCase
from unittest.mock import patch
from npc import shawn


class TestShawn(TestCase):
    @patch('builtins.input', side_effect=["y", "y"])
    def test_shawn(self, _):
        character = {"shawn_quest": True, "elixir": 2, "heca_found": True}
        shawn(character)
        expected = {"shawn_quest": False, "elixir": 5, "heca_found": True}
        self.assertEqual(expected, character)
