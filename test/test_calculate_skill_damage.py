from unittest import TestCase
from combat import calculate_skill_damage
from unittest.mock import patch
from io import StringIO


class TestCalculateSkillDamage(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculate_skill_damage_invalid(self, mock_stdout):
        skill = "Fireball"
        chosen_type = "normal"
        character = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,
                     'chris': False}
        creature = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass', 'golds': 5,
                    'tree_branches': 3}
        calculate_skill_damage(skill, chosen_type, character, creature)
        expected = 'Unknown skill\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_calculate_skill_damage_valid_citizen(self):
        skill = "Tackle"
        chosen_type = "normal"
        character = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,
                     'chris': False}
        creature = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass', 'golds': 5,
                    'tree_branches': 3}
        result = calculate_skill_damage(skill, chosen_type, character, creature)
        expected = 7.5
        self.assertEqual(result, expected)

    def test_calculate_skill_damage_valid_hero(self):
        # when character has a class other than default Citizen
        skill = "Ice Age"
        chosen_type = "fire"
        character = {'class': 'Magician', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},
                     'level': 1, 'exp': 0, 'skills':
                         {"Ice Age": "water", "Inferno Sphere": "fire", "Poison Nova": "grass", "Elixir": "normal"},
                     "type": "fire", 'hp': 100, 'max_hp': 100, 'elixir': 1, 'gold': 0, 'shawn_quest': None,
                     'david_quest': None, 'heca_found': False, 'tree_branches': 0, 'chris': False}
        creature = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass', 'golds': 5,
                    'tree_branches': 3}
        result = calculate_skill_damage(skill, chosen_type, character, creature)
        expected = 30
        self.assertEqual(result, expected)
