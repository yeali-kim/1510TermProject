from unittest import TestCase
from unittest.mock import patch
from combat import tree_branches
from io import StringIO


class TestTreeBranches(TestCase):
    def test_tree_branches_character(self):
        character = {"tree_branches": 1, 'david_quest': True}
        monster = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass',
                   'golds': 5, 'tree_branches': 2}
        tree_branches(character, monster)
        expected = {"tree_branches": 3, 'david_quest': True}
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tree_branches_print(self, mock_stdout):
        character = {"tree_branches": 1, 'david_quest': True}
        monster = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass',
                   'golds': 5, 'tree_branches': 2}
        tree_branches(character, monster)
        expected = "You got 2 tree branches.\n"\
                   "Now you have 3 branches\n"
        self.assertEqual(expected, mock_stdout.getvalue())



