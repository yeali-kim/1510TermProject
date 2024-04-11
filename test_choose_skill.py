from unittest import TestCase
from unittest.mock import patch
from combat import choose_skill


class TestChooseSkill(TestCase):
    @patch('builtins.input', return_value='1')
    def test_choose_skill_valid(self, _):
        character = {'class': "Archer",
                     "skills": {"Fire Arrow": "fire",
                                "Frost Arrow": "water",
                                "Storm of Arrows": "normal",
                                "Elixir": "normal"}
                     }
        expected = ('Fire Arrow', 'fire')
        actual = choose_skill(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Fire Arrow', 1])
    def test_choose_skill_invalid_then_valid(self, _):
        character = {'class': "Archer",
                     "skills": {"Fire Arrow": "fire",
                                "Frost Arrow": "water",
                                "Storm of Arrows": "normal",
                                "Elixir": "normal"}
                     }
        expected = ('Fire Arrow', 'fire')
        actual = choose_skill(character)
        self.assertEqual(expected, actual)
