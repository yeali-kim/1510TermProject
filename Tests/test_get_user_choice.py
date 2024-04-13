from unittest import TestCase
from unittest.mock import patch
from character_functions import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["up", "w"])
    def test_get_user_choice_invalid_then_valid(self, _):
        expected = "up"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["", "$", "d"])
    def test_get_user_choice_empty_invalid_valid(self, _):
        expected = "right"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["a"])
    def test_get_user_choice_valid(self, _):
        expected = "left"
        actual = get_user_choice()
        self.assertEqual(actual, expected)
