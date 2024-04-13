from unittest import TestCase
from character_functions import create_character
from unittest.mock import patch


class TestCreateCharacter(TestCase):
    @patch('character_functions.random.randint')
    def test_create_character(self, mock_randint):
        mock_randint.side_effect = [5, 5, 5]
        expected = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                    'level': 1, 'exp': 0, 'skills': {'Elixir': 'normal', 'Tackle': 'normal'}, 'hp': 100,
                    'max_hp': 100, 'elixir': 1, 'gold': 0, 'shawn_quest': None, 'david_quest': None,
                    'heca_found': False, 'tree_branches': 0, 'chris': False}
        actual = create_character()
        self.assertEqual(expected, actual)

