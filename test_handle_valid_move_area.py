from unittest import TestCase
from character_functions import handle_valid_move_area
from io import StringIO
from unittest.mock import patch


class Test(TestCase):
    def test_handle_valid_move_area(self):
        character = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,
                     'chris': False}
        current_area = 'Desert'
        new_area = 'Desert'
        new_x, new_y = 1, 0
        handle_valid_move_area(character, current_area, new_area, new_x, new_y)
        expected = {'chris': False,
                    'class': 'Citizen',
                    'david_quest': None,
                    'elixir': 1,
                    'exp': 0,
                    'gold': 0,
                    'heca_found': False,
                    'hp': 100,
                    'level': 1,
                    'location': {'x-coordinate': 1, 'y-coordinate': 0},
                    'max_hp': 100,
                    'shawn_quest': None,
                    'skills': {'Tackle': 'normal'},
                    'stats': [5, 5, 5],
                    'tree_branches': 0}
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_valid_move_area_same_print(self, mock_stdout):
        character = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,
                     'chris': False}
        current_area = 'Desert'
        new_area = 'Desert'
        new_x, new_y = 1, 0
        handle_valid_move_area(character, current_area, new_area, new_x, new_y)
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_valid_move_area_diff_print(self, mock_stdout):
        character = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,
                     'chris': False}
        current_area = 'Desert'
        new_area = 'Castle'
        new_x, new_y = 1, 0
        handle_valid_move_area(character, current_area, new_area, new_x, new_y)
        expected = ("Now you move from Desert to Castle. Be careful Castle is dangerous\n"
                    "Moving to Castle...\n")
        self.assertEqual(expected, mock_stdout.getvalue())







