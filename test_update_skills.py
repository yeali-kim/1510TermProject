from unittest import TestCase
from character_functions import update_skills


class TestUpdateSkills(TestCase):
    def test_update_skills(self):
        expected = ""
        character = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                    'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,
                    'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,
                    'chris': False}
        actual = update_skills(character)
        self.assertEqual(expected, actual)

