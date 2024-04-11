from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from combat import drink_elixir


class TestDrinkElixir(TestCase):
    def test_drink_elixir_have(self):
        character = {'elixir': 5, 'hp': 30, 'max_hp': 100}
        drink_elixir(character)
        expected = {'elixir': 4, 'hp': 100, 'max_hp': 100}
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=StringIO)
    def test_drink_elixir_not_have(self, mock_stdout):
        character = {'elixir': 0, 'hp': 30, 'max_hp': 100}
        drink_elixir(character)
        expected = "You don't have any elixir...\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_drink_elixir_have_print(self, mock_stdout):
        character = {'elixir': 5, 'hp': 30, 'max_hp': 100}
        drink_elixir(character)
        expected = ("Your hp is full now!\n"
                    "Now you have 4\n")
        self.assertEqual(expected, mock_stdout.getvalue())

