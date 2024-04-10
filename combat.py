import random
import character_functions


def create_creature(region: str) -> dict[str, int | str] | None:
    # Define basic attributes for creatures in each region
    creatures = {
        'Forest': [
            {'name': 'Rabbit', 'health': 10, 'damage': 5, 'exp': 50, 'type': 'grass',
             'golds': random.randint(1, 5)},
            {'name': 'Gump', 'health': 20, 'damage': 10, 'exp': 60, 'type': 'normal',
             'golds': random.randint(2, 8)},
            {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 70, 'type': 'grass',
             'golds': random.randint(5, 10), 'tree_branches': random.randint(1, 3)},
            {'name': 'Wild Boar', 'health': 50, 'damage': 20, 'exp': 80, 'type': 'grass',
             'golds': random.randint(7, 12)},
        ],
        'Desert': [
            {'name': 'Scorpion', 'health': 100, 'damage': 30, 'exp': 150, "type": "fire",
             "golds": random.randint(10, 15)},
            {'name': 'Skeleton', 'health': 200, 'damage': 50, 'exp': 200, "type": "normal",
             "golds": random.randint(12, 17)},
            {'name': 'Golem', 'health': 300, 'damage': 70, 'exp': 300, "type": "water",
             "golds": random.randint(15, 20)},
            {'name': 'Sand Serpent', 'health': 500, 'damage': 100, 'exp': 250, "type": "normal",
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
        probability = [3, 6, 8, 10]
        for index, threshold in enumerate(probability):
            if creature_number <= threshold:
                selected_creature = creatures[region][index]
                message = "A wild" if region != 'Castle' else "A guardian"
                print(f"{message} {selected_creature['name']} appears!")
                return selected_creature
    else:
        return None


def calculate_skill_damage(skill: str, chosen_type: str, character: dict, creature: dict) -> int:
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
        "Elixir": drink_elixir(character)
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
        ('fire', 'other'): 0.5,
    }
    if skill in skill_damage_formulas:
        multiplier = types[(creature["type"], chosen_type)]
        damage = skill_damage_formulas[skill] * multiplier
        return damage
    else:
        print("Unknown skill")
        return 0


def choose_skill(character: dict[str, str | int | bool | dict[str, int]]) -> tuple[str, str]:
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
    return chosen_skill_name, character['skills'][chosen_skill_name]


def drink_elixir(character: dict[str, str | int | bool | dict[str, int]]):
    if character['elixir'] > 0:
        character['hp'] = character['max_hp']
        character["elixir"] -= 1
        print("Your hp is full now!")
        print(f"Now you have {character['elixir']}")
        return 0
    else:
        print("You don't have any elixir...")
        return 0


def engage_combat(character: dict[str, str | int | bool | dict[str, int]], creature: dict[str, int | str]):
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
            break


def is_alive(character: dict[str, str | int | bool | dict[str, int]]) -> bool:
    return False if character["hp"] <= 0 else True


def tree_branches(character: dict[str, str | int | bool | dict[str, int]], creature: dict[str, int | str]):
    if creature["name"] == "Stump" and character["david_quest"]:
        character["tree_branches"] += creature["tree_branches"]
        print(f"You got {creature['tree_branches']} tree branches.")
        print(f"Now you have {character['tree_branches']} branches")


def handle_encounter(character: dict[str, str | int | bool | dict[str, int]], board: dict[tuple[int, int], str]):
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
    if random.random() < 0.5:  # 50% chance to escape
        print("You managed to escape safely.")
    else:
        print("Failed to escape. Forced into combat.")
        engage_combat(character, creature)


def main_combat(creature: dict[str, int | str], character: dict[str, str | int | bool | dict[str, int]]):
    action = input("Do you wish to fight (f) or try to run (r)? ")

    if action.lower() == 'f':
        engage_combat(character, creature)

        if creature['health'] <= 0:
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
        engage_combat(character, creature)
