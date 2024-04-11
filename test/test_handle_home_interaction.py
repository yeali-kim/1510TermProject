from unittest.mock import patch
from unittest import TestCase
from character_functions import handle_home_interaction
from io import StringIO


class TestHandleHomeInteraction(TestCase):
    def test_handle_home_interaction_return(self):
        character = {'hp': 50, 'max_hp': 100}
        handle_home_interaction(character)
        self.assertEqual(character, {'hp': 100, 'max_hp': 100})

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_home_interaction_print(self, mock_stdout):
        character = {'hp': 50, 'max_hp': 100}
        handle_home_interaction(character)
        expected = "Your hp is full now.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
