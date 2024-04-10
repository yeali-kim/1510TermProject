import random
from operator import call
import npc


def create_character() -> dict[str, str | int | bool | dict[str, int]]:
    """
    Create and initialize a character with default settings.

    :precondition: random module must be imported
    :postcondition: a fully initialized character dictionary with all necessary attributes set to their default or
    randomized starting values
    :return: a dictionary of character's default information
    """
    character_class = "Citizen"

    citizen_skill = {
        "Citizen": {
            "Tackle": "normal",
            "Elixir": "normal"
        }
    }

    classes = {
        "Citizen": {"str": random.randint(1, 10), "dex": random.randint(1, 10),
                    "int": random.randint(1, 10), "hp": 100, "max_hp": 100},
    }

    # Initialize the character with class-specific stats, location, level, Exp, and skills
    user_character = {
        "class": character_class,
        "stats": [classes[character_class]['str'], classes[character_class]['dex'], classes[character_class]['int']],
        "location": {"x-coordinate": 6, "y-coordinate": 2},  # Default location at home
        "level": 1,  # Starting level
        "exp": 0,  # Starting experience points
        "skills": citizen_skill[character_class],
        "hp": classes[character_class]["hp"],
        "max_hp": classes[character_class]["max_hp"],
        "elixir": 1,  # Starting elixir
        "gold": 0,  # Starting money
        "shawn_quest": None,
        "david_quest": None,
        "heca_found": False,
        "tree_branches": 0,
        "chris": False
    }

    return user_character


def update_skills(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Update the character's skill based on their class.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must have a class key with a valid class name as its value
    :postcondition: the skills key in the character dictionary is updated to reflect the skills corresponding to
    the character's class
    >>> player= {"class": "Knight"}
    >>> update_skills(player)
    >>> player["skills"]
    {'Shield Attack': 'normal', 'Fire Sword': 'fire', 'Guillotine': 'normal', 'Elixir': 'normal'}
    >>> player= {"class": "Archer"}
    >>> update_skills(player)
    >>> player["skills"]
    {'Fire Arrow': 'fire', 'Frost Arrow': 'water', 'Storm of Arrows': 'normal', 'Elixir': 'normal'}
    """
    skills = {
        "Guardian": {
            "Tackle": "normal",
            "Sword of Justice": "normal"
        },
        "Knight": {
            "Shield Attack": "normal",
            "Fire Sword": "fire",
            "Guillotine": "normal",
            "Elixir": "normal"
        },
        "Archer": {
            "Fire Arrow": "fire",
            "Frost Arrow": "water",
            "Storm of Arrows": "normal",
            "Elixir": "normal"
        },
        "Magician": {
            "Ice Age": "water",
            "Inferno Sphere": "fire",
            "Poison Nova": "grass",
            "Elixir": "normal"
        },
        "Devil": {
            "Hell Fire": "fire",
            "Abracadabra": "normal",
        }
    }
    character["skills"] = skills[character["class"]]


def update_level(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Update the character's level and stats based on their accumulated experience points.

    :param character: a dictionary representing a character
    :precondition: character must be a well-defined dictionary with all necessary keys and values for level progression
    :postcondition: if the character has sufficient experience for a level up, their level is increased,
    and appropriate stat increases are applied based on their class
    the character's exp is adjusted to remove the amount used for leveling up.
    >>> player = {"class": "Citizen", "level": 1, "exp": 100, "stats": [1, 1, 1], "max_hp": 100}
    >>> update_level(player)
    Congratulations! Your character is now level 2.
    Your stats have increased:
    Strength: 2, Dexterity: 2, Intelligence: 2, HP: 120
    You need 101 more Exp to reach level 3.
    >>> player = {"class": "Magician", "level": 10, "exp": 300, "stats": [10, 11, 15], "max_hp": 300}
    >>> update_level(player)
    Congratulations! Your character is now level 11.
    Your stats have increased:
    Strength: 10, Dexterity: 11, Intelligence: 35, HP: 410
    Congratulations! Your character is now level 12.
    Your stats have increased:
    Strength: 10, Dexterity: 11, Intelligence: 55, HP: 530
    You need 31 more Exp to reach level 13.
    """
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

        class_growth = {
            "Citizen": {"stats": [1, 1, 1], "hp_growth_factor": 10},
            "Knight": {"stats": [10, 5, 0], "hp_growth_factor": 15},
            "Archer": {"stats": [5, 15, 0], "hp_growth_factor": 12},
            "Magician": {"stats": [0, 0, 20], "hp_growth_factor": 10},
        }

        growth_info = class_growth.get(character["class"], None)

        if growth_info:
            for i, stat_growth in enumerate(growth_info["stats"]):
                character["stats"][i] += stat_growth

            character["max_hp"] += character["level"] * growth_info["hp_growth_factor"]
            character["hp"] = character["max_hp"]
            print("Your stats have increased:")
            print(f"Strength: {character["stats"][0]}, Dexterity: {character["stats"][1]},"
                  f" Intelligence: {character["stats"][2]}, HP: {character["hp"]}")
        else:
            print(f"No growth info for class: {character['class']}")

        # Check for another level up in case of remaining Exp
        update_level(character)
    else:
        print(f"You need {exp_for_next_level - character["exp"]} more Exp to reach level {character["level"] + 1}.")


def get_user_choice() -> str:
    """
    Get the direction from the user of where they want to move their character in.

    :precondition: The character coordinate must be within the board dimension
    :postcondition: request user input for the direction to move the character in
    :return: a string that is one of "Up", "Down", "Left", and "Right"
    """
    directions = {"w": "up", "s": "down", "a": "left", "d": "right"}
    user_direction = input("Enter movement direction (w, a, s, d) or 'quit' to exit: ")
    while user_direction not in directions:
        user_direction = input("Enter movement direction (w, a, s, d) or 'quit' to exit: ")
    direction = directions[user_direction]
    return direction


def calculate_new_position(x: int, y: int, direction: str, movement: dict[str, tuple[int, int]]) -> tuple[int, int]:
    """
    Calculate character's new position

    :param x: the current x-coordinate of the character as an integer
    :param y: the current x-coordinate of the character as an integer
    :param direction: a string indicating the direction in which the character is moving
    :param movement: a dictionary where each key is a direction and each value is a tuple of two integers
    :precondition: x and y must be integers representing the current position of the character
    direction should be a string that matches one of the keys in the 'movement' dictionary
    movement must be a dictionary with string keys (directions) and tuple values indicating movement offsets
    :postcondtion:
    :return:
    """
    value_of_coordinates = movement.get(direction, (0, 0))
    new_x = x + value_of_coordinates[0]
    new_y = y + value_of_coordinates[1]
    return new_x, new_y


def is_valid_move(new_x: int, new_y: int, game_board: dict[tuple[int, int], str]) -> bool:
    """
    Check character's move is valid or not

    :param new_x:
    :param new_y:
    :param game_board:
    :precondition:
    :postcondition:
    :return:
    """
    return (new_x, new_y) in game_board


def handle_valid_move_area(character, current_area, new_area, new_x: int, new_y: int):
    if current_area in ["Forest", "Desert", "Castle"] and new_area in ["Forest", "Desert", "Castle"]:
        print(f"Now you move from {current_area} to {new_area}. Be careful {new_area} is dangerous")
    print(f"Moving to {new_area}...")
    character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y


def handle_door_interaction(character: dict[str, str | int | bool | dict[str, int]], door_to: str, current_area: str,
                            new_x: int, new_y: int):
    if current_area == "Town" and door_to == "Forest":
        print("Before you go to Forest, I strongly recommend you to get a class!")
        print("You can go to school left of the Town to get great skills")
        decision = ask_for_confirmation("Are you sure to enter the Forest? Y/N ")
        if decision:
            print("Be careful... the Forest is mysterious and full of dangers.")
            move_character_to_new_position(character, new_x, new_y)
        else:
            print("Come back when you are ready...")

    elif current_area == "Town" and door_to == "Desert":
        decision = ask_for_confirmation("Are you sure to enter the Desert? Recommended level: 10 Y/N ")
        if decision:
            print("Be careful... the Desert is harsh and unforgiving.")
            move_character_to_new_position(character, new_x, new_y)
        else:
            print("Come back when you are ready...")

    else:
        move_character_to_new_position(character, new_x, new_y)
        print(f"You are moving through the door to {door_to}.")


def handle_home_interaction(character: dict[str, str | int | bool | dict[str, int]]):
    character["hp"] = character["max_hp"]
    print("Your hp is full now.")


def interact_with_npc(character: dict[str, str | int | bool | dict[str, int]], npc_name: str):
    func_name = getattr(npc, npc_name)
    call(func_name, character)


def ask_for_confirmation(prompt: str) -> bool:
    user_input = ""
    valid_input = ["y", "n"]
    while user_input not in valid_input:
        user_input = input(prompt).lower()
    return user_input == "y"


def move_character_to_new_position(character: dict[str, str | int | bool | dict[str, int]], new_x: int, new_y: int):
    character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y


def move_character(character: dict[str, str | int | bool | dict[str, int]], direction: str,
                   game_board: dict[tuple[int, int], str]):
    movement = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
    valid_move = ["Town", "School", "Forest", "Desert", "Castle"]

    x, y = character["location"]["x-coordinate"], character["location"]["y-coordinate"]

    new_x, new_y = calculate_new_position(x, y, direction, movement)

    if not is_valid_move(new_x, new_y, game_board):
        print("Invalid move. Out of bounds.")
        return

    new_area = game_board[(new_x, new_y)]
    current_area = game_board[(x, y)]

    if new_area in valid_move:
        handle_valid_move_area(character, current_area, new_area, new_x, new_y)
    elif new_area in ["horizontal_wall", "vertical_wall"]:
        print("Invalid move. You've hit a wall.")
    elif "Door" in new_area:
        door_to = new_area.split(" ")[2]
        handle_door_interaction(character, door_to, current_area, new_x, new_y)
    elif new_area == "home":
        handle_home_interaction(character)
    else:
        interact_with_npc(character, new_area)
