from unittest import TestCase
from character_functions import calculate_new_position


class TestCalculateNewPosition(TestCase):
    def test_calculate_new_position_up(self):
        x = 1
        y = 1
        direction = "up"
        movement = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        result = calculate_new_position(x, y, direction, movement)
        expected = (1, 0)
        self.assertEqual(expected, result)

    def test_calculate_new_position_left(self):
        x = 1
        y = 1
        direction = "left"
        movement = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        result = calculate_new_position(x, y, direction, movement)
        expected = (0, 1)
        self.assertEqual(expected, result)
