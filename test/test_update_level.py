from unittest import TestCase
from character_functions import update_level
from unittest.mock import patch
from io import StringIO


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

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_level_level_no_up_print(self, mock_stdout):
        player = {"class": "Citizen", "level": 1, "exp": 90, "stats": [1, 1, 1], "max_hp": 100}
        update_level(player)
        expected = "You need 10 more Exp to reach level 2.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_level_level_up_print(self,mock_stdout):
        player = {"class": "Citizen", "level": 1, "exp": 100, "stats": [1, 1, 1], "max_hp": 100}
        update_level(player)
        expected = ("Congratulations! Your character is now level 2.\n"
                    "Your stats have increased:\n"
                    "Strength: 2, Dexterity: 2, Intelligence: 2, HP: 120\n"
                    "You need 101 more Exp to reach level 3.\n")
        self.assertEqual(expected, mock_stdout.getvalue())



        
