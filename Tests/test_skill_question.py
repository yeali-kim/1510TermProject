from unittest import TestCase
from unittest.mock import patch
from npc import skill_question


class TestSkillQuestion(TestCase):
    @patch('random.choice', return_value='rat')
    def test_skill_question(self, _):
        actual = skill_question()
        expected = 'rat'
        self.assertEqual(expected, actual)
