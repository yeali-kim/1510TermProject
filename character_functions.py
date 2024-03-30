import random
from operator import call
import npc
import combat
import board


def create_character():
    character_class = "Citizen"

    citizen_skill = {
        "Citizen": {
            "Tackle": "normal"
        }
    }

    classes = {
        "Citizen": {"str": random.randint(1, 10), "dex": random.randint(1, 10),
                    "int": random.randint(1, 10), "hp": 100, "max_hp": 100},
    }

    # Initialize the character with class-specific stats, location, level, Exp, and skills
    user_character = {
        "class": character_class,
        "stats": [classes[character_class]['str'], classes[character_class]['dex'], classes[character_class]['int'],],
        "location": {"x-coordinate": 6, "y-coordinate": 2},  # Default location at home
        "level": 1,  # Starting level
        "exp": 0,  # Starting experience points
        "skills": citizen_skill[character_class],
        "hp": classes[character_class]["hp"],
        "max_hp": classes[character_class]["max_hp"],
        "elixir": 1,  # Starting elixir
        "money": 0,  # Starting money
        "shawn_quest": None,
        "david_quest": False,
        "heca_found": False,
        "tree branches": 0
    }

    return user_character


def update_skills(character):
    skills = {
        "Citizen": {
            "Tackle": "normal"
        },
        "Knight": {
            "Shield Attack": "normal",
            "Fire Sword": "fire",
            "Guillotine": "normal"
        },
        "Archer": {
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
    character["skills"] = skills[character["class"]]


def update_level(character):
    # Base experience required for the first level up
    base_exp_per_level = 100
    # Experience growth rate for each subsequent level
    exp_growth_rate = 1.01  # 1% more Exp required for each level

    # Calculate the current required Exp for the next level
    exp_for_next_level = round(base_exp_per_level * (exp_growth_rate ** (character["level"] - 1)))

    # Check if the character has enough Exp to level up
    if character["exp"] >= exp_for_next_level:
        character["exp"] -= exp_for_next_level  # Deduct the Exp used to level up
        character["level"] += 1  # Increase level

        # Print level-up message
        print(f"Congratulations! Your character is now level {character["level"]}.")

        # Stat increases depend on character class
        if character["class"] == "Citizen":
            character["stats"][0] += 1  # str stat
            character["stats"][1] += 1  # dex stat
            character["stats"][2] += 1  # int stat
            character["max_hp"] += character["level"] * 10
            character["hp"] = character["max_hp"]
        elif character["class"] == "Knight":
            character["stats"][0] += 10     # str stat
            character["stats"][1] += 5      # dex stat
            character["max_hp"] += character["level"] * 15
            character["hp"] = character["max_hp"]
        elif character["class"] == "Archer":
            character["stats"][0] += 10     # str stat
            character["stats"][1] += 15     # dex stat
            character["max_hp"] += character["level"] * 12
            character["hp"] = character["max_hp"]
        elif character["class"] == "Magician":
            character["stats"][2] += 20     # int stat
            character["max_hp"] += character["level"] * 10
            character["hp"] = character["max_hp"]

        print("Your stats have increased:")
        print(f"Strength: {character["stats"][0]}, Dexterity: {character["stats"][1]},"
              f" Intelligence: {character["stats"][2]}, HP: {character["hp"]}")

        # Check for another level up in case of remaining Exp
        update_level(character)
    else:
        print(f"You need {exp_for_next_level - character["exp"]} more Exp to reach level {character["level"] + 1}.")


def get_user_choice():
    user_input = ""
    while user_input not in ["up", "down", "left", "right", "quit", "elixir"]:
        user_input = input("Enter movement direction (up, down, left, right) or 'elixir'"
                           " to drink elixir or 'quit' to exit: ")
        user_input = user_input.lower()
    return user_input


def move_character(character, direction, board):
    valid_move = ["Town", "School", "Forest", "Desert", "Castle"]
    # Current location
    x, y = character["location"]["x-coordinate"], character["location"]["y-coordinate"]
    # Calculate new location based on the direction
    new_x, new_y = x, y

    if direction == "up":
        new_y -= 1
    elif direction == "down":
        new_y += 1
    elif direction == "left":
        new_x -= 1
    elif direction == "right":
        new_x += 1

    # Check for out-of-bounds
    if (new_x, new_y) not in board:
        print("Invalid move. Out of bounds.")
        return

    # Allow movement if it's within the same region, through a door, or from home
    if board[(new_x, new_y)] in valid_move:
        print(f"Moving to {board[(new_x, new_y)]}...")
        character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
    elif board[(new_x, new_y)] == "horizontal_wall" or board[(new_x, new_y)] == "vertical_wall":
        print("Invalid move. You've hit a wall.")
    elif board[(new_x, new_y)] == "Door to School":
        if board[(x, y)] == "Town":
            print("You are moving through the door to School.")
        else:
            print("You are moving through the door to Town.")
        character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
    elif board[(new_x, new_y)] == "Door to Forest":
        if board[(x, y)] == "Town":
            user_input = ""
            valid_input = ["y", "n"]
            while user_input not in valid_input:
                user_input = input("Are you sure to enter the Forest? Y/N ")
                user_input = user_input.lower()
            if user_input == "y":
                character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
                print("Be careful...")
            else:
                print("Come back when you are ready...")
        else:
            character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
            print("You are moving through the door to Town.")
    elif board[(new_x, new_y)] == "Door to Desert":
        if board[(x, y)] == "Town":
            user_input = ""
            valid_input = ["y", "n"]
            while user_input not in valid_input:
                user_input = input("Are you sure to enter the Desert? Y/N ")
                user_input = user_input.lower()
            if user_input == "y":
                character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
                print("Be careful... Desert is dangerous....")
            else:
                print("Come back when you are ready...")
        else:
            character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
            print("You are moving through the door to Town.")
    elif board[(new_x, new_y)] == "home":
        character["hp"] = character["max_hp"]
        print("Your hp is full now.")
    else:
        func_name = getattr(npc, board[(new_x, new_y)]) # Call the function based on the NPC name
        call(func_name, character)
