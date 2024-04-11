from unittest import TestCase
from unittest.mock import patch
from npc import david


class TestDavid(TestCase):
    @patch('builtins.input', side_effect=["y", "y"])
    def test_david(self, _):
        character = {"david_quest": True, "gold": 100, "tree_branches": 10}
        david(character)
        expected = {"david_quest": False, "gold": 200, "tree_branches": 0}
        self.assertEqual(expected, character)
