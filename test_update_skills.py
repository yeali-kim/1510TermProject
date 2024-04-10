from unittest import TestCase
from character_functions import update_skills


import unittest

class TestUpdateSkills(unittest.TestCase):
    def test_update_skills_knight(self):
        character_knight = {"class": "Knight"}
        update_skills(character_knight)
        self.assertEqual(character_knight["skills"], {
            "Shield Attack": "normal",
            "Fire Sword": "fire",
            "Guillotine": "normal"
        })

    def test_update_skills_archer(self):
        character_archer = {"class": "Archer"}
        update_skills(character_archer)
        self.assertEqual(character_archer["skills"], {
            "Fire Arrow": "fire",
            "Frost Arrow": "water",
            "Storm of Arrows": "normal"
        })


    def test_update_skills_magician(self):
        character_magician = {"class": "Magician"}
        update_skills(character_magician)
        self.assertEqual(character_magician["skills"], {
            "Ice Age": "water",
            "Inferno Sphere": "fire",
            "Poison Nova": "grass"
        })
        
    def test_update_skills_devil(self):
        character_devil = {"class": "Devil"}
        update_skills(character_devil)
        self.assertEqual(character_devil["skills"], {
            "Hell Fire": "fire",
            "Abracadabra": "normal"
        })
        
    def test_update_skills_guardian(self):
        character_guardian = {"class": "Guardian"}
        update_skills(character_guardian)
        self.assertEqual(character_guardian["skills"], {
            "Tackle": "normal",
            "Sword of Justice": "normal"
        })
