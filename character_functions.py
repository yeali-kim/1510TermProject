import random
from operator import call
import npc
import combat
import board


def create_character():
    # Mapping of input numbers to character classes
    # class_options = {1: 'Knight', 2: 'Archer', 3: 'Magician'}
    character_class = 'Citizen'

    citizen_skill = {
        'Citizen': {
            'Tackle': 'normal'
        }
    }

    # Attempt to get user input and validate it
    # while character_class is None:
    #     try:
    #         choice = int(input("Enter the number that you want for your class - 1. Knight, 2. Archer, 3. Magician: "))
    #         if choice in class_options:
    #             character_class = class_options[choice]
    #         else:
    #             print("Invalid choice. Please enter a number between 1 and 3.")
    #     except ValueError:
    #         print("Please enter a valid number to choose your class!")

    classes = {
        'Citizen': {'str': random.randint(1, 10), 'dex': random.randint(1, 10),
                    'int': random.randint(1, 10), 'hp': 100, 'max_hp': 100},

    }

    # Initialize the character with class-specific stats, location, level, Exp, and skills
    user_character = {
        'class': character_class,
        'stats': classes[character_class],
        'location': {'x-coordinate': 6, 'y-coordinate': 2},  # Default location at home
        'level': 1,  # Starting level
        'exp': 0,  # Starting experience points
        'skills': citizen_skill[character_class],
        'hp': classes[character_class]['hp'],
        'max_hp': classes[character_class]['max_hp'],
        'potion': 1,  # Starting potion
        "money": 0  # Starting money
    }

    return user_character


def update_skills(character):
    skills = {
        'Citizen': {
            'Tackle': 'normal'
        },
        'Knight': {
            'Shield Attack': 'normal',
            'Fire Sword': 'fire',
            'Guillotine': 'normal'
        },
        'Archer': {
            "Fire Arrow": "fire",
            "Frost Arrow": "water",
            "Storm of Arrows": "normal"
        },
        "Magician": {
            "Ice Age": "water",
            "Inferno Sphere": "fire",
            "Poison Nova": "grass",
        }
    }
    character["skills"] = skills[character['class']]


def update_level(character):
    # Base experience required for the first level up
    base_exp_per_level = 100
    # Experience growth rate for each subsequent level
    exp_growth_rate = 1.05  # 5% more Exp required for each level
    # base hp to calculate total hp when character leveled up
    base_hp = {
        'Citizen': 100,
        'Knight': 150,
        'Archer': 100,
        'Magician': 80,
    }

    # Calculate the current required Exp for the next level
    exp_for_next_level = base_exp_per_level * (exp_growth_rate ** (character['level'] - 1))

    # Check if the character has enough Exp to level up
    if character['exp'] >= exp_for_next_level:
        character['exp'] -= exp_for_next_level  # Deduct the Exp used to level up
        character['level'] += 1  # Increase level

        # Print level-up message
        print(f"Congratulations! Your character is now level {character['level']}.")

        # Stat increases depend on character class
        if character['class'] == 'Citizen':
            character['stats']['str'] += 1
            character['stats']['dex'] += 1
            character['stats']['int'] += 1
            # 10% increase hp
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level'] - 1) / 10)), 0)
            character['hp'] = character['max_hp']
        elif character['class'] == 'Knight':
            character['stats']['str'] += 2
            character['stats']['dex'] += 1
            # 10% increase hp
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level'] - 1) / 10)), 0)
            character['hp'] = character['max_hp']
        elif character['class'] == 'Archer':
            character['stats']['str'] += 1
            character['stats']['dex'] += 4
            # 10% increase hp
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level'] - 1) / 10)), 0)
            character['hp'] = character['max_hp']
        elif character['class'] == 'Magician':
            character['stats']['dex'] += 2
            character['stats']['int'] += 3
            # 10% increase hp
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level'] - 1) / 10)), 0)
            character['hp'] = character['max_hp']

        print("Your stats have increased:")
        print(f"Strength: {character['stats']['str']}, Dexterity: {character['stats']['dex']}, \
        Intelligence: {character['stats']['int']}, HP: {character['hp']}")

        # Check for another level up in case of remaining Exp
        update_level(character)
    else:
        print(f"You need {exp_for_next_level - character['exp']} more Exp to reach level {character['level'] + 1}.")


def get_user_choice():
    user_input = ""
    while user_input not in ["up", "down", "left", "right", "quit", "potion"]:
        user_input = input("Enter movement direction (up, down, left, right) or 'potion' to drink potion or 'quit' to "
                           "exit: ")
        user_input = user_input.lower()
    return user_input


def move_character(character, direction, board):
    valid_move = ['Town', 'School', 'Forest', 'Desert', 'Castle']
    # Current location
    x, y = character['location']['x-coordinate'], character['location']['y-coordinate']
    # Calculate new location based on the direction
    new_x, new_y = x, y

    if direction == 'up':
        new_y -= 1
    elif direction == 'down':
        new_y += 1
    elif direction == 'left':
        new_x -= 1
    elif direction == 'right':
        new_x += 1

    # Check for out-of-bounds
    if (new_x, new_y) not in board:
        print("Invalid move. Out of bounds.")
        return

    # Allow movement if it's within the same region, through a door, or from home
    if board[(new_x, new_y)] in valid_move:
        print(f"Moving to {board[(new_x, new_y)]}...")
        character['location']['x-coordinate'], character['location']['y-coordinate'] = new_x, new_y
    elif board[(new_x, new_y)] == 'horizontal_wall' or board[(new_x, new_y)] == 'vertical_wall':
        print("Invalid move. You've hit a wall.")
    elif board[(new_x, new_y)] == 'home':
        character['hp'] = character['max_hp']
        print("Your hp is full now.")
    else:
        func_name = getattr(npc, board[(new_x, new_y)])
        call(func_name, character)
