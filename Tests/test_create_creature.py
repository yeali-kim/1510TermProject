from unittest import TestCase
from combat import create_creature
from unittest.mock import patch
from io import StringIO


class TestCreateCreature(TestCase):
    @patch('combat.random.randint')
    def test_create_creature_forest_stump(self, mock_randint):
        mock_randint.side_effect = [1, 2, 5, 3, 7, 10, 12, 15, 20, 20, 25, 30, 35, 7]
        creature = create_creature('Forest')
        expected_creature = ({'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass',
                             'golds': 5, 'tree_branches': 3})
        self.assertEqual(creature, expected_creature)

    @patch('combat.random.randint')
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_creature_forest_stump_print(self, mock_stdout, mock_randint):
        mock_randint.side_effect = [1, 2, 5, 3, 7, 10, 12, 15, 20, 20, 25, 30, 35, 7]
        create_creature('Forest')
        expected = 'A wild Stump appears!\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('combat.random.randint')
    def test_create_creature_desert_golem(self, mock_randint):
        mock_randint.side_effect = [1, 2, 5, 3, 7, 10, 12, 15, 20, 20, 25, 30, 35, 7]
        creature = create_creature('Desert')
        expected_creature = ({'name': 'Golem', 'health': 300, 'damage': 70, 'exp': 300, "type": "water",
                              "golds": 15})
        self.assertEqual(creature, expected_creature)

    @patch('combat.random.randint')
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_creature_desert_golem_print(self, mock_stdout, mock_randint):
        mock_randint.side_effect = [1, 2, 5, 3, 7, 10, 12, 15, 20, 20, 25, 30, 35, 7]
        create_creature('Desert')
        expected = 'A wild Golem appears!\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('combat.random.randint')
    def test_create_creature_castle_cerberus(self, mock_randint):
        mock_randint.side_effect = [1, 2, 5, 3, 7, 10, 12, 15, 20, 20, 25, 30, 35, 2]
        creature = create_creature('Castle')
        expected_creature = ({'name': 'Cerberus', 'health': 700, 'damage': 200, 'exp': 500, "type": "fire",
                              "golds": 20})
        self.assertEqual(creature, expected_creature)

    @patch('combat.random.randint')
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_creature_castle_cerberus_print(self, mock_stdout, mock_randint):
        mock_randint.side_effect = [1, 2, 5, 3, 7, 10, 12, 15, 20, 20, 25, 30, 35, 2]
        create_creature('Castle')
        expected = 'A guardian Cerberus appears!\n'
        self.assertEqual(expected, mock_stdout.getvalue())
