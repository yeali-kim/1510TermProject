from unittest import TestCase
from unittest.mock import patch
from character_functions import ask_for_confirmation


class Test(TestCase):
    @patch('builtins.input', side_effect=["yes", "y"])
    def test_ask_for_confirmation_invalid_valid(self, _):
        expected = True
        actual = ask_for_confirmation("Do you want to proceed?")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["y"])
    def test_ask_for_confirmation_y(self, _):
        expected = True
        actual = ask_for_confirmation("Do you want to proceed?")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["n"])
    def test_ask_for_confirmation_n(self, _):
        expected = False
        actual = ask_for_confirmation("Do you want to proceed?")
        self.assertEqual(expected, actual)
