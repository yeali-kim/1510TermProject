import random
import character_functions
import time

import itertools


def create_creature(region: str) -> dict[str, int | str] | None:
    """
    Randomly generates a creature based on the specified region with predefined attributes.

    :param region: a string indicating the region from which to generate a creature.
    :precondition: the region parameter must correspond to a key in the predefined creatures dictionary
    :postcondition: if the region is valid, a creature dictionary containing the creature's attributes is returned
    :postcondition: the specific creature is chosen based on a randomized probability distribution
    :postcondition: if the specified region is not recognized, the function returns None
    :postcondition: a message is printed indicating the appearance of the creature
    :return: a dictionary with the selected creature's attributes if the region is valid; otherwise, None
    """
    # Define basic attributes for creatures in each region
    creatures = {
        'Forest': [
            {'name': 'Rabbit', 'health': 10, 'damage': 5, 'exp': 80, 'type': 'grass',
             'golds': random.randint(1, 5)},
            {'name': 'Gump', 'health': 20, 'damage': 10, 'exp': 100, 'type': 'normal',
             'golds': random.randint(2, 8)},
            {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 120, 'type': 'grass',
             'golds': random.randint(5, 10), 'tree_branches': random.randint(1, 3)},
            {'name': 'Wild Boar', 'health': 50, 'damage': 20, 'exp': 130, 'type': 'grass',
             'golds': random.randint(7, 12)},
        ],
        'Desert': [
            {'name': 'Scorpion', 'health': 100, 'damage': 30, 'exp': 150, "type": "fire",
             "golds": random.randint(10, 15)},
            {'name': 'Skeleton', 'health': 200, 'damage': 50, 'exp': 200, "type": "normal",
             "golds": random.randint(12, 17)},
            {'name': 'Golem', 'health': 300, 'damage': 70, 'exp': 300, "type": "water",
             "golds": random.randint(15, 20)},
            {'name': 'Sand Serpent', 'health': 500, 'damage': 100, 'exp': 350, "type": "normal",
             "golds": random.randint(20, 25)},

        ],
        'Castle': [
            {'name': 'Cerberus', 'health': 700, 'damage': 200, 'exp': 500, "type": "fire",
             "golds": random.randint(20, 25)},
            {'name': 'Gargoyle', 'health': 1000, 'damage': 300, 'exp': 800, "type": "normal",
             "golds": random.randint(25, 30)},
            {'name': 'Lich', 'health': 1000, 'damage': 700, 'exp': 1000, "type": "water",
             "golds": random.randint(30, 35)},
            {'name': 'Death Knight', 'health': 2000, 'damage': 500, 'exp': 1500, "type": "normal",
             "golds": random.randint(35, 40)},
        ]
    }

    if region in creatures:
        creature_number = random.randint(1, 10)
        probability = [3, 6, 8, 10]  # 30%, 30%, 20%, 20%
        for index, threshold in zip(itertools.count(0), probability):  # proof of concept
            if creature_number <= threshold:
                selected_creature = creatures[region][index]
                message = "A wild" if region != 'Castle' else "A guardian"
                print(f"{message} {selected_creature['name']} appears!")
                return selected_creature
    else:
        return None


def calculate_skill_damage(skill: str, chosen_type: str, character: dict[str, str | int | bool | dict[str, int]],
                           creature: dict[str, int | str]) -> int:
    """
    Calculates the damage inflicted by a specific skill used by a character against a creature, factoring in the
    character's stats and the type advantages between the character's chosen type and the creature's type.

    :param skill: a string representing the skill used by the character
    :param chosen_type: a string representing the chosen type of the character for the skill interaction
    :param character: a dictionary representing a character
    :param creature: a dictionary representing a creature
    :precondition: skill must be the key in the skill_damage_formulas dictionary
    :precondition: chosen_type and the creature's type must be a valid key in the type dictionary
    :precondition: the character dictionary must have a stats key
    :precondition: the creature dictionary must have a type key with a valid type string
    :postcondition: calculate and return the damage as an integer, based on the character's stats, the skill used,
    and the type advantage multiplier.
    :return: an integer representing the calculated damage and returns 0 for an unknown skill
    >>> skill_name = "Tackle"
    >>> user_chosen_type = "normal"
    >>> player = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},\
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,\
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,\
                     'chris': False}
    >>> creature_type = {"type": "normal"}
    >>> calculate_skill_damage(skill_name, user_chosen_type, player, creature_type)
    7.5
    >>> skill_name = "Poison Nova"
    >>> user_chosen_type = "grass"
    >>> player = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},\
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,\
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,\
                     'chris': False}
    >>> creature_type = {"type": "fire"}
    >>> calculate_skill_damage(skill_name, user_chosen_type, player, creature_type)
    -7.5
    """
    skill_damage_formulas = {
        'Tackle': character['stats'][0] * 0.5 + character['stats'][1] * 0.5 + character['stats'][2] * 0.5,
        "Sword of Justice": character["stats"][0] * 100 + character["stats"][1] * 100 + character["stats"][2] * 100,

        'Shield Attack': character['stats'][0] * 1.5 + character['stats'][1] * 2,
        "Fire Sword": character["stats"][0] * 2,
        "Guillotine": character["stats"][0] * 3,

        'Fire Arrow': character['stats'][1] * 4,
        "Frost Arrow": character["stats"][1] * 4,
        "Storm of Arrows": character["stats"][1] * 4 + character["stats"][0] * 2,

        'Ice Age': character['stats'][2] * 3,
        "Inferno Sphere": character["stats"][2] * 3,
        "Poison Nova": character["stats"][2] * 3,

        "Hell Fire": character["stats"][0] * 100 + character["stats"][1] * 100 + character["stats"][2] * 100,
        "Abracadabra": character["stats"][0] * 100 + character["stats"][1] * 100 + character["stats"][2] * 100,
        "Elixir": 0
    }
    types = {
        ('grass', 'normal'): 1,
        ('grass', 'grass'): 0.5,
        ('grass', 'water'): -0.5,
        ('grass', 'fire'): 2,
        ('normal', 'normal'): 1,
        ('normal', 'grass'): 1,
        ('normal', 'water'): 1,
        ('normal', 'fire'): 1,
        ('water', 'normal'): 1,
        ('water', 'grass'): 2,
        ('water', 'water'): 0.5,
        ('water', 'fire'): -0.5,
        ('fire', 'normal'): 1,
        ('fire', 'grass'): -0.5,
        ('fire', 'water'): 2,
        ('fire', 'fire'): 0.5,
    }
    if skill in skill_damage_formulas:
        multiplier = types[(creature["type"], chosen_type)]
        damage = skill_damage_formulas[skill] * multiplier
        return damage
    else:
        print("Unknown skill")
        return 0


def choose_skill(character: dict[str, str | int | bool | dict[str, int]]) -> tuple[str, str] | int:
    """
    Prompts the user to choose a skill from the character's available skills and returns the selected skill's name
    and type.

    :param character: a dictionary representing a character
    :precondition: character must have a skills key with a dictionary value
    :precondition: if Elixir is chosen by user, a function called drink_elixir must exist and accept the character
    dictionary as a parameter
    :postcondition: if a valid skill other than Elixir is chosen, the function returns a tuple containing
    the skill's name and type
    :postcondition: if Elixir is chosen, the drink_elixir function will be called
    :return: a tuple containing the chosen skill's name and type
    """
    print("Available skills:")
    skills_list = list(character['skills'].keys())  # Convert skill names to a list
    for skill_number in range(len(skills_list)):
        print(f"{skill_number + 1}. {skills_list[skill_number]}")

    skill_choice = 0
    while skill_choice < 1 or skill_choice > len(skills_list):
        try:
            skill_choice = int(input("Choose a skill to use (number): "))
            if skill_choice < 1 or skill_choice > len(skills_list):
                print(f"Please enter a number between 1 and {len(skills_list)}.")
        except ValueError:
            print("Please enter a valid number.")

    # Return the chosen skill name and type as a tuple
    chosen_skill_name = skills_list[skill_choice - 1]
    if chosen_skill_name == "Elixir":
        return drink_elixir(character)
    return chosen_skill_name, character['skills'][chosen_skill_name]


def drink_elixir(character: dict[str, str | int | bool | dict[str, int]]) -> tuple[str, str]:
    """
    Restores the character's health points to maximum if an elixir is available and decreases the elixir count by one.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must contain hp, max_hp, and elixir keys with integer values
    :postcondition: if elixir is greater than 0, hp is set to max_hp, elixir is decremented by one,
    and a success message is printed
    :postcondition: if elixir is 0, a failure message is printed indicating that no elixirs are available
    :return: a tuple containing the string "Elixir" and its type "normal"
    >>> player = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},\
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,\
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,\
                     'chris': False}
    >>> drink_elixir(player)
    Your hp is full now!
    Now you have 0
    ('Elixir', 'normal')
    >>> player = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},\
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 0,\
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,\
                     'chris': False}
    >>> drink_elixir(player)
    You don't have any elixir...
    ('Elixir', 'normal')
    """
    if character['elixir'] > 0:
        character['hp'] = character['max_hp']
        character["elixir"] -= 1
        print("Your hp is full now!")
        time.sleep(1)
        print(f"Now you have {character['elixir']}")
        time.sleep(1)
        return "Elixir", "normal"
    else:
        print("You don't have any elixir...")
        time.sleep(1)
        return "Elixir", "normal"


def engage_combat(character: dict[str, str | int | bool | dict[str, int]], creature: dict[str, int | str]):
    """
    Simulates combat between the character and a creature, allowing the character to use skills against the creature.

    :param character: a dictionary representing a character
    :param creature: a dictionary representing a creature
    :precondition: character must have hp and skills keys
    :precondition: creature must be properly initialized with name, health, and damage
    :postcondition: combat continues in turns until the character or the creature's health is reduced to zero or below
    :postcondition: if the creature's health is reduced to zero or below first, a victory message is printed
    :postcondition: if the character's health is reduced to zero or below, print a game over message
    """
    print(f"Engaging in combat with {creature['name']}...")

    while creature['health'] > 0:
        # Let the user choose a skill
        chosen_skill, chosen_type = choose_skill(character)
        damage_dealt = calculate_skill_damage(chosen_skill, chosen_type, character, creature)

        print(f"Using {chosen_skill}, you deal {damage_dealt} damage to the {creature['name']}.")

        # Apply damage to the creature
        creature['health'] -= damage_dealt
        if creature['health'] <= 0:
            print(f"You've defeated the {creature['name']}!")
            break
        print(f"{creature['name']} is still alive with {creature['health']} health left.")
        character['hp'] -= creature['damage']
        print(f"{creature['name']} deal {creature['damage']} to you")
        print(f"After the {creature['name']}'s attack, your HP is now {character['hp']}.")
        if character['hp'] <= 0:
            print("Game Over")
            time.sleep(1)
            break


def tree_branches(character: dict[str, str | int | bool | dict[str, int]], creature: dict[str, int | str]):
    """
    Rewards the character with tree branches if they defeat a 'Stump' creature while on the 'David' quest.

    :param character: a dictionary representing a character
    :param creature: a dictionary representing a creature
    :precondition: the character dictionary must contain a david_quest key that indicates
    whether the quest is active or not
    :precondition: the creature dictionary must contain a name key that matches Stump
    :precondition: the Stump should include a tree_branches key
    :postcondition: if the conditions ar met, the number of tree_branches in the character's inventory is increased
    :postcondition: print notifications how many tree branches got and have
    >>> player = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},\
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,\
                     'gold': 0, 'shawn_quest': None, 'david_quest': True, 'heca_found': False, 'tree_branches': 0,\
                     'chris': False}
    >>> monster = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass',\
             'golds': 5, 'tree_branches': 2}
    >>> tree_branches(player, monster)
    You got 2 tree branches.
    Now you have 2 branches
    >>> print(player)
    {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2}, 'level': 1, 'exp': 0,\
 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1, 'gold': 0, 'shawn_quest': None,\
 'david_quest': True, 'heca_found': False, 'tree_branches': 2, 'chris': False}

    >>> player = {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2},\
                     'level': 1, 'exp': 0, 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1,\
                     'gold': 0, 'shawn_quest': None, 'david_quest': None, 'heca_found': False, 'tree_branches': 0,\
                     'chris': False}
    >>> monster = {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass',\
             'golds': 5, 'tree_branches': 2}
    >>> tree_branches(player, monster)
    >>> print(player)
    {'class': 'Citizen', 'stats': [5, 5, 5], 'location': {'x-coordinate': 6, 'y-coordinate': 2}, 'level': 1, 'exp': 0,\
 'skills': {'Tackle': 'normal'}, 'hp': 100, 'max_hp': 100, 'elixir': 1, 'gold': 0, 'shawn_quest': None,\
 'david_quest': None, 'heca_found': False, 'tree_branches': 0, 'chris': False}

    """
    if creature["name"] == "Stump" and character["david_quest"]:
        character["tree_branches"] += creature["tree_branches"]
        print(f"You got {creature['tree_branches']} tree branches.")
        time.sleep(1)
        print(f"Now you have {character['tree_branches']} branches")


def handle_encounter(character: dict[str, str | int | bool | dict[str, int]], board: dict[tuple[int, int], str]):
    """
    Simulates an encounter with a creature when the character moves into certain locations on the board.

    :param character: a dictionary representing a character
    :param board: a dictionary mapping (x, y) coordinated tuples to strings describing the area
    :precondition: the character dictionary must include a location key
    :precondition: the board dictionary must include keys for all valid locations
    :postcondition: if an encounter occurs, the function generates a creature using "create_creature" function
    :postcondition: if no encounter occurs, a simple message is printed
    """
    x, y = character['location']['x-coordinate'], character['location']['y-coordinate']
    current_location_type = board[(x, y)]

    if current_location_type in ['Forest', 'Desert', 'Castle']:
        if random.random() < 0.8:  # 80% chance of encounter
            creature = create_creature(current_location_type)
            print(f"You've encountered a {creature['name']}!")
            print(f"The {creature['name']} is {creature['type']} type")
            main_combat(creature, character)
        else:
            print("It's quiet... too quiet.")


def run_combat(character: dict[str, str | int | bool | dict[str, int]],
               creature: dict[str, str | int | bool | dict[str, int]]):
    """
    Attempts to escape from combat with a creature based on a randomized chance.

    :param character: a dictionary representing a character
    :param creature: a dictionary representing a creature
    :precondition: the "engage_combat" function must exist and accept the character dictionary and creature dictionary
     as a parameter
    :postcondition: if the escape is successful, a safe notification message is printed
    :postcondition: if the escape fails, "engage_combat" is called
    """
    if random.random() < 0.5:  # 50% chance to escape
        print("You managed to escape safely.")
    else:
        print("Failed to escape. Forced into combat.")
        time.sleep(1)
        engage_combat(character, creature)


def main_combat(creature: dict[str, int | str], character: dict[str, str | int | bool | dict[str, int]]):
    """
    Manages the main combat loop, allowing the player to choose between fighting or running from a creature encounter.

    :param creature: a dictionary representing a creature
    :param character: a dictionary representing a character
    :precondition: creature must have health, exp, and gold keys
    :precondition: character must include keys for exp, gold, and may include specific quest-related items or conditions
    :postcondition: if the player chooses to fight and wins, character is updated with gained exp, golds,
    and quest specific items
    :postcondition: if the player attempts to run and the attempt fails, engage_combat is automatically called
    :postcondition: the character's level may be updated if the gained exp from defeating the creature is sufficient
    for leveling up
    """
    action = input("Do you wish to fight (f) or try to run (r)? ")

    if action.lower() == 'f':
        engage_combat(character, creature)
        gained_exp = creature['exp']  # Use the creature's exp value
        character['exp'] += gained_exp
        print(f"You gained {gained_exp} Exp!")
        character["gold"] += creature["golds"]  # Add creature's gold
        print(f"You got {creature['golds']} golds")
        tree_branches(character, creature)
        character_functions.update_level(character)  # Check and handle level up

    elif action.lower() == 'r':
        run_combat(character, creature)
    else:
        print("Invalid action. You're forced into combat.")
        time.sleep(1)
        engage_combat(character, creature)
