from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from npc import get_valid_elixir_quantity


class TestGetValidElixirQuantity(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['one', 1])
    def test_get_valid_elixir_quantity_invalid_print(self, _, mock_output):
        get_valid_elixir_quantity('How many do you want to buy?:')
        expected = "You need to enter a valid integer greater than 0.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['', 1])
    def test_get_valid_elixir_quantity_empty(self, _, mock_output):
        get_valid_elixir_quantity('How many do you want to buy?:')
        expected = "You need to enter a valid integer greater than 0.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['-1', 1])
    def test_get_valid_elixir_quantity_negative(self, _, mock_output):
        get_valid_elixir_quantity('How many do you want to buy?:')
        expected = "Quantity must be an integer greater than 0.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', return_value='1')
    def test_get_valid_elixir_valid(self, _):
        actual = get_valid_elixir_quantity('How many do you want to buy?:')
        expected = 1
        self.assertEqual(expected, actual)
