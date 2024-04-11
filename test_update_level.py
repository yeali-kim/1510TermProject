from unittest import TestCase
from character_functions import update_level


class TestUpdateLevel(TestCase):
    def test_update_level_one_level(self):
        player = {"class": "Citizen", "level": 1, "exp": 100, "stats": [1, 1, 1], "max_hp": 100}
        update_level(player)
        expected = {'class': 'Citizen',
                    'exp': 0,
                    'hp': 120,
                    'level': 2,
                    'max_hp': 120,
                    'stats': [2, 2, 2]}
        self.assertEqual(expected, player)

    def test_update_level_more_levels(self):
        player = {"class": "Magician", "level": 10, "exp": 300, "stats": [10, 11, 15], "max_hp": 300}
        update_level(player)
        expected = {'class': 'Magician',
                    'exp': 81,
                    'hp': 530,
                    'level': 12,
                    'max_hp': 530,
                    'stats': [10, 11, 55]}
        self.assertEqual(expected, player)

        
