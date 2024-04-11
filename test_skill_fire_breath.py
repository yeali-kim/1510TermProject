from unittest import TestCase
from npc import skill_fire_breath
from unittest.mock import patch


class TestSkillFireBreath(TestCase):
    @patch('builtins.input', return_value='up')
    @patch('npc.random.choice', return_value='up')
    def test_skill_fire_breath_match(self, _, __):
        character = {"hp": 1000}
        skill_fire_breath(character)
        expected = {"hp": 300}
        self.assertEqual(expected, character)

    @patch('builtins.input', return_value='up')
    @patch('npc.random.choice', return_value='down')
    def test_skill_fire_breath_no_match(self, _, __):
        character = {"hp": 1000}
        skill_fire_breath(character)
        expected = {"hp": 1000}
        self.assertEqual(expected, character)
