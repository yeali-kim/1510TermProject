import random
from operator import call
import npc


def create_character() -> dict[str, str | int | bool | dict[str, int]]:
    character_class = "Citizen"

    citizen_skill = {
        "Citizen": {
            "Tackle": "normal"
        }
    }

    classes = {
        "Citizen": {"str": random.randint(1000000000, 10000000000), "dex": random.randint(1, 10),
                    "int": random.randint(1, 10), "hp": 10000000, "max_hp": 10000000},
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
    skills = {
        "Citizen": {
            "Tackle": "normal",
            "Guardian of Justice": "normal"
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
        },
        "Devil": {
            "Hell Fire": "fire",
            "Abracadabra": "normal",
        }
    }
    character["skills"] = skills[character["class"]]


def update_level(character: dict[str, str | int | bool | dict[str, int]]):
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
            character["stats"][0] += 10  # str stat
            character["stats"][1] += 5  # dex stat
            character["max_hp"] += character["level"] * 15
            character["hp"] = character["max_hp"]
        elif character["class"] == "Archer":
            character["stats"][0] += 10  # str stat
            character["stats"][1] += 15  # dex stat
            character["max_hp"] += character["level"] * 12
            character["hp"] = character["max_hp"]
        elif character["class"] == "Magician":
            character["stats"][2] += 20  # int stat
            character["max_hp"] += character["level"] * 10
            character["hp"] = character["max_hp"]

        print("Your stats have increased:")
        print(f"Strength: {character["stats"][0]}, Dexterity: {character["stats"][1]},"
              f" Intelligence: {character["stats"][2]}, HP: {character["hp"]}")

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
    user_direction = input("Enter movement direction (w, a, s, d) or 'elixir' to drink elixir or 'quit' to exit: ")
    while user_direction not in directions:
        user_direction = input(
            "Enter movement direction (w, a, s, d) or 'elixir' to drink elixir or 'quit' to exit: ")
    direction = directions[user_direction]
    return direction


def calculate_new_position(x: int, y: int, direction: str, movement: dict[str, tuple[int, int]]) -> tuple[int, int]:
    value_of_coordinates = movement.get(direction, (0, 0))
    new_x = x + value_of_coordinates[0]
    new_y = y + value_of_coordinates[1]
    return new_x, new_y


def is_valid_move(new_x: int, new_y: int, game_board: dict[tuple[int, int], str]) -> bool:
    return (new_x, new_y) in game_board


def handle_valid_move_area(character, current_area, new_area, new_x: int, new_y: int):
    if current_area in ["Forest", "Desert", "Castle"] and new_area in ["Forest", "Desert", "Castle"]:
        print(f"Now you move from {current_area} to {new_area}. Be careful {new_area} is dangerous")
    print(f"Moving to {new_area}...")
    character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y


def handle_wall_collision():
    print("Invalid move. You've hit a wall.")


def handle_door_interaction(character, door_to, current_area: str, new_x: int, new_y: int):
    if current_area == "Town" and door_to == "Forest":
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


def ask_for_confirmation(prompt: str):
    user_input = ""
    valid_input = ["y", "n"]
    while user_input not in valid_input:
        user_input = input(prompt).lower()
    return user_input == "y"


def move_character_to_new_position(character: dict[str, str | int | bool | dict[str, int]], new_x: int, new_y: int):
    character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y


def move_character(character: dict[str, str | int | bool | dict[str, int]], direction: str, game_board: dict[tuple[int, int], str]):
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
        handle_wall_collision()
    elif "Door" in new_area:
        door_to = new_area.split(" ")[2]
        handle_door_interaction(character, door_to, current_area, new_x, new_y)
    elif new_area == "home":
        handle_home_interaction(character)
    else:
        interact_with_npc(character, new_area)

# def move_character(character, direction: str, game_board: dict[tuple[int, int], str]):
#     valid_move = ["Town", "School", "Forest", "Desert", "Castle"]
#     movement = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
#     # Current location
#     x, y = character["location"]["x-coordinate"], character["location"]["y-coordinate"]
#     # Calculate new location based on the direction
#     value_of_coordinates = movement.get(direction, (0, 0))
#     new_x, new_y = x + value_of_coordinates[0], y + value_of_coordinates[1]
#
#     # Check for out-of-bounds
#     if (new_x, new_y) not in game_board:
#         print("Invalid move. Out of bounds.")
#         return
#     new_area = game_board[(new_x, new_y)]
#     current_area = game_board[(x, y)]
#     # Allow movement if it's within the same region, through a door, or from home
#     if new_area in valid_move:
#         if current_area in ["Forest", "Desert", "Castle"] and new_area in ["Forest", "Desert", "Castle"]:
#             print(f"Now you move from {current_area} to {new_area}. Be careful {new_area} is dangerous")
#         print(f"Moving to {new_area}...")
#         character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
#     elif new_area in ["horizontal_wall", "vertical_wall"]:
#         print("Invalid move. You've hit a wall.")
#     elif new_area == "Door to School":
#         if current_area == "Town":
#             print("You are moving through the door to School.")
#         else:
#             print("You are moving through the door to Town.")
#         character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
#     elif new_area == "Door to Forest":
#         if current_area == "Town":
#             user_input = ""
#             valid_input = ["y", "n"]
#             while user_input not in valid_input:
#                 user_input = input("Are you sure to enter the Forest? Y/N ")
#                 user_input = user_input.lower()
#             if user_input == "y":
#                 character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
#                 print("Be careful...")
#             else:
#                 print("Come back when you are ready...")
#         else:
#             character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
#             print("You are moving through the door to Town.")
#     elif new_area == "Door to Desert":
#         if current_area == "Town":
#             user_input = ""
#             valid_input = ["y", "n"]
#             while user_input not in valid_input:
#                 user_input = input("Are you sure to enter the Desert? Recommended lever: 10 Y/N ")
#                 user_input = user_input.lower()
#             if user_input == "y":
#                 character["location"]["x-coordinate"], character["location"]["y-coordinate"] = new_x, new_y
#                 print("Be careful... Desert is dangerous....")
#             else:
#                 print("Come back when you are ready...")
#     elif new_area == "home":
#         character["hp"] = character["max_hp"]
#         print("Your hp is full now.")
#     else:
#         func_name = getattr(npc, new_area)  # Call the function based on the NPC name
#         call(func_name, character)
