import random
from operator import call
import npc
import time


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
                    "int": random.randint(1, 10), "hp": 100, "max_hp": 100
                    },
    }
    # Initialize the character with class-specific stats, location, level, Exp, and skills
    user_character = {
        "class": character_class,
        "stats": [classes[character_class]['str'], classes[character_class]['dex'], classes[character_class]['int']],
        "location": {"x-coordinate": 6, "y-coordinate": 2},  # Default location at home
        "level": 1,
        "exp": 0,
        "skills": citizen_skill[character_class],
        "hp": classes[character_class]["hp"],
        "max_hp": classes[character_class]["max_hp"],
        "elixir": 1,
        "gold": 0,
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
    :postcondition: the character's exp is adjusted to remove the amount used for leveling up.
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
        print(f"Congratulations! You are now \033[1;33m level {character["level"]}\033[0m.")
        time.sleep(1)

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
            time.sleep(1)
            print(f"Strength: {character["stats"][0]}, Dexterity: {character["stats"][1]},"
                  f" Intelligence: {character["stats"][2]}, HP: {character["hp"]}")
            time.sleep(1)
        else:
            print(f"No growth info for class: {character['class']}")
            time.sleep(1)
        # Call function until exp runs out
        update_level(character)
    else:
        print(f"You need {exp_for_next_level - character["exp"]} more Exp to reach level {character["level"] + 1}.")
        time.sleep(1)


def get_user_choice() -> str:
    """
    Get the direction from the user of where they want to move their character in.

    :precondition: The character coordinate must be within the board dimension
    :postcondition: request user input for the direction to move the character in
    :return: a string that is one of "Up", "Down", "Left", and "Right"
    """
    directions = {"w": "up", "s": "down", "a": "left", "d": "right", "quit": "quit"}
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
    :precondition: direction should be a string that matches one of the keys in the 'movement' dictionary
    :precondition: movement must be a dictionary with string keys (directions)
    and tuple values indicating movement offsets
    :postcondtion: a tuple of two integers representing the new position of the character.
    :return: a tuple (new_x, new_y) representing the new coordinates of the character after the movement.
    >>> calculate_new_position(1, 1, "up", {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)})
    (1, 0)
    >>> calculate_new_position(1, 1, "left", {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)})
    (0, 1)
    """
    value_of_coordinates = movement.get(direction, (0, 0))
    new_x = x + value_of_coordinates[0]
    new_y = y + value_of_coordinates[1]
    return new_x, new_y


def handle_valid_move_area(character: dict[str, str | int | bool | dict[str, int]], current_area: str, new_area: str,
                           new_x: int, new_y: int):
    """
    Update the character's location and provide feedback on moving between different areas.

    :param character: a dictionary representing a character
    :param current_area: a string representing the area the character is currently in
    :param new_area: a string representing the area the character intends to move to
    :param new_x: the new x-coordinate (integer) for the character in the new area
    :param new_y: the new y-coordinate (integer) for the character in the new area
    :precondition: character must be a dictionary that includes location information
    :precondition: current_area and new_area should be among the predefined valid areas
    :postcondition: prints a message indicating the character is moving and includes a warning
    :postcondition: updates the character's location key with the new x and y coordinates
    >>> player = {"location": {"x-coordinate": 1, "y-coordinate": 1}}
    >>> current = "Forest"
    >>> new = "Desert"
    >>> new_x_coordinate, new_y_coordinate = 1, 0
    >>> handle_valid_move_area(player, current, new, new_x_coordinate, new_y_coordinate)
    Now you move from Forest to Desert. Be careful Desert is dangerous
    Moving to Desert...
    >>> player = {"location": {"x-coordinate": 1, "y-coordinate": 1}}
    >>> current = "Desert"
    >>> new = "Desert"
    >>> new_x_coordinate, new_y_coordinate = 1, 0
    >>> handle_valid_move_area(player, current, new, new_x_coordinate, new_y_coordinate)
    """
    if current_area != new_area:
        if current_area in ["Forest", "Desert", "Castle"] and new_area in ["Forest", "Desert", "Castle"]:
            print(f"Now you move from {current_area} to {new_area}. Be careful {new_area} is dangerous")
            time.sleep(1.5)
        print(f"Moving to {new_area}...")
        time.sleep(1.5)
    character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y


def handle_door_interaction(character: dict[str, str | int | bool | dict[str, int]], door_to: str, current_area: str,
                            new_x: int, new_y: int):
    """
    Handle character interactions with doors leading to different areas, providing narrative prompts and updating the
    character's location based on decisions.

    :param character: a dictionary representing a character
    :param door_to: a string representing the name of the next area the character intends to enter
    :param current_area: a string representing the area the character is currently in
    :param new_x: the new x-coordinate (integer) for the character in the new area
    :param new_y: the new y-coordinate (integer) for the character in the new area
    :precondition: character must be a dictionary with a location key that includes x-coordinate and y-coordinate
    :precondition: current_area and door_to should be valid area names within the game's world
    :precondition: new_x and new_y should be integers representing valid coordinates
    :postcondition: if moving from Town to Forest or Desert, the function prompts the player for confirmation
    :postcondition: if confirmed, the character's location is updated
    :postcondition: for all other area transitions, the character's location is updated directly to the new coordinates
    """
    if current_area == "Town" and door_to == "Forest" and character["class"] == "Citizen":
        print("Before you enter the Forest, I strongly recommend you to obtain a class!")
        time.sleep(1.5)
        print("You can go to school located next to the Town to get great skills.")
        time.sleep(1.5)
        decision = ask_for_confirmation("Are you sure to enter the Forest? Y/N ")
        if decision:
            print("Be careful... the Forest is mysterious and full of dangers.")
            time.sleep(1.5)
            character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
        else:
            print("Come back when you are ready...")

    elif current_area == "Town" and door_to == "Desert":
        decision = ask_for_confirmation("Are you sure to enter the Desert? Recommended level: 10. Y/N ")
        if decision:
            print("Be careful... the Desert is harsh and unforgiving.")
            time.sleep(1.5)
            character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
        else:
            print("Come back when you are ready...")
            time.sleep(1.5)

    else:
        character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
        print(f"You are moving through the door to {door_to}.")
        time.sleep(1.5)


def handle_home_interaction(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Restores the character's health points to their maximum when they interact with their home.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must exist and contain hp and max_hp keys, hp and max_hp must be integers
    :postcondition: the character's hp is set equal to their max_hp, effectively restoring the character's hp to full
    a message is printed to notify the player of the health restoration
    >>> player = {"hp": 100, "max_hp": 100}
    >>> handle_home_interaction(player)
    Your hp is full now.
    """
    character["hp"] = character["max_hp"]
    print("Your hp is full now.")
    time.sleep(1.5)


def interact_with_npc(character: dict[str, str | int | bool | dict[str, int]], npc_name: str):
    """
    Handle the character's interaction with a Non-Player Character (NPC) by calling a specific function associated
    with the NPC's name.

    :param character: a dictionary representing a character
    :param npc_name: a string representing the name of the NPC
    :precondition: each function should accept a single argument: a character dictionary
    :postcondition: the function associated with 'npc_name' within the 'npc' object or module is called,
    passing 'character' as an argument.
    """
    func_name = getattr(npc, npc_name)
    call(func_name, character)


def ask_for_confirmation(prompt: str) -> bool:
    """
    Prompts the user with a question and expects a 'yes' or 'no' response.

    :param prompt: a string containing the question or message to present to the user
    :precondition: the prompt should be a string
    :postcondition: the user is repeatedly prompted until a valid input (y or n) is provided
    :return: a boolean value representing the user's response. True for y and False for n
    """
    user_input = ""
    valid_input = ["y", "n"]
    while user_input not in valid_input:
        user_input = input(prompt).lower()
    return user_input == "y"


def move_character(character: dict[str, str | int | bool | dict[str, int]], direction: str,
                   game_board: dict[tuple[int, int], str]):
    """
    Move the character in the specified direction and handle interactions based on the new location.

    :param character: a dictionary representing a character
    :param direction: a string indicating the direction in which the character is moving
    :param game_board: a dictionary mapping (x, y) coordinated tuples to strings describing the area
    :precondition: character must have valid location with current coordinates
    :precondition: direction must be one of the specified valid directions (up, down, left, right)
    :precondition: game_board must accurately represent the current game state, with coordinates
    :postcondition: if the move is valid and leads to an area that triggers a specific interaction,
    the corresponding interaction function is called
    :postcondition: if the move is invalid, an appropriate message is printed, and no position update is made
    """
    movement = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
    valid_move = ["Town", "School", "Forest", "Desert", "Castle"]

    x, y = character["location"]["x-coordinate"], character["location"]["y-coordinate"]

    new_x, new_y = calculate_new_position(x, y, direction, movement)

    if (new_x, new_y) not in game_board:
        print("Invalid move. Out of bounds.")
        time.sleep(1)
        return

    new_area = game_board[(new_x, new_y)]
    current_area = game_board[(x, y)]

    if new_area in valid_move:
        handle_valid_move_area(character, current_area, new_area, new_x, new_y)
    elif new_area in ["horizontal_wall", "vertical_wall"]:
        print("Invalid move. You've hit a wall.")
        time.sleep(1)
    elif "Door" in new_area:
        door_to = new_area.split(" ")[2]
        handle_door_interaction(character, door_to, current_area, new_x, new_y)
    elif new_area == "home":
        handle_home_interaction(character)
    else:
        interact_with_npc(character, new_area)
