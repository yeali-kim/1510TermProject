from unittest import TestCase
from unittest.mock import patch
from npc import skill_question


class TestSkillQuestion(TestCase):
    @patch('npc.random.choice')
    @patch('builtins.input')
    def test_skill_question_right(self, mock_input, mock_choice):
        character = {"max_hp": 300}
        skill_question(character)
        mock_choice.return_value = "rat"
        mock_input.return_value = "rat"
        expected = {"max_hp": 200}
        self.assertEqual(expected, character)
