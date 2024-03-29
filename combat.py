import random
import character_functions


def create_creature(region):
    # Define basic attributes for creatures in each region
    creatures = {
        'Forest': [
            {'name': 'Rabbit', 'health': 10, 'damage': 5, 'exp': 10, 'type': 'grass', 'golds': random.randint(1, 5)},
            {'name': 'Gump', 'health': 20, 'damage': 10, 'exp': 15, 'type': 'normal', 'golds': random.randint(2, 8)},
            {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 20, 'type': 'grass', 'golds': random.randint(5, 10)},
            {'name': 'Wild Boar', 'health': 50, 'damage': 20, 'exp': 30, 'type': 'grass',
             'golds': random.randint(7, 12)},
        ],
        'Desert': [
            {'name': 'Scorpion', 'health': 100, 'damage': 30, 'exp': 80, "type": "fire",
             "golds": random.randint(10, 15)},
            {'name': 'Skeleton', 'health': 200, 'damage': 50, 'exp': 100, "type": "normal",
             "golds": random.randint(12, 17)},
            {'name': 'Golem', 'health': 300, 'damage': 70, 'exp': 150, "type": "water",
             "golds": random.randint(15, 20)},
            {'name': 'Sand Serpent', 'health': 500, 'damage': 100, 'exp': 250, "type": "normal",
             "golds": random.randint(20, 25)},

        ],
        'Castle': [
            {'name': 'Cerberus', 'health': 700, 'damage': 200, 'exp': 500, "type": "fire",
             "gold": random.randint(20, 25)},
            {'name': 'Gargoyle', 'health': 1000, 'damage': 300, 'exp': 800, "type": "normal",
             "gold": random.randint(25, 30)},
            {'name': 'Lich', 'health': 1000, 'damage': 700, 'exp': 1000, "type": "water",
             "gold": random.randint(30, 35)},
            {'name': 'Death Knight', 'health': 2000, 'damage': 500, 'exp': 1500, "type": "normal",
             "gold": random.randint(35, 40)},
        ]
    }

    if region == 'Forest':
        # Randomly select a creature from the specified region
        creature = random.randint(1, 10)
        if creature <= 3:
            creature = creatures['Forest'][0]
        elif creature <= 6:
            creature = creatures['Forest'][1]
        elif creature <= 8:
            creature = creatures['Forest'][2]
        else:
            creature = creatures['Forest'][3]
        print(f"A wild {creature['name']} appears!")
        return creature
    elif region == 'Desert':
        creature = random.randint(1, 10)
        if creature <= 3:
            creature = creatures['Desert'][0]
        elif creature <= 6:
            creature = creatures['Desert'][1]
        elif creature <= 8:
            creature = creatures['Desert'][2]
        else:
            creature = creatures['Desert'][3]
        print(f"A wild {creature['name']} appears!")
        return creature
    elif region == 'Castle':
        creature = random.randint(1, 10)
        if creature <= 3:
            creature = creatures['Castle'][0]
        elif creature <= 6:
            creature = creatures['Castle'][1]
        elif creature <= 8:
            creature = creatures['Castle'][2]
        else:
            creature = creatures['Castle'][3]
        print(f"A guardian {creature['name']} appears!")
        return creature
    else:
        print("No creatures found in this region.")
        return None


def calculate_skill_damage(skill, chosen_type, character, creature):
    skill_damage_formulas = {
        'Tackle': character['stats']['str'] * 0.5 + character['stats']['dex'] * 0.5 + character['stats']['int'] * 0.5,

        'Shield Attack': character['stats']['str'] * 1.5 + character['stats']['dex'] * 2,
        "Fire Sword": character["stats"]["str"] * 2,
        "Guillotine": character["stats"]["str"] * 3,

        'Fire Arrow': character['stats']['dex'] * 4,
        "Frost Arrow": character["stats"]["dex"] * 4,
        "Storm of Arrows": character["stats"]["dex"] * 4 + character["stats"]["str"] * 2,

        'Ice Age': character['stats']['int'] * 3,
        "Inferno Sphere": character["stats"]["int"] * 3,
        "Poison Nova": character["stats"]["int"] * 3,
    }
    if skill in skill_damage_formulas:
        if creature['type'] == 'grass':
            if chosen_type == 'normal':
                damage = skill_damage_formulas[skill] * 1
                return damage
            elif chosen_type == 'grass':
                damage = skill_damage_formulas[skill] * 0.5
                return damage
            elif chosen_type == 'water':
                damage = skill_damage_formulas[skill] * -0.5
                return damage
            else:
                damage = skill_damage_formulas[skill] * 2
                return damage
        elif creature['type'] == 'normal':
            if chosen_type == 'normal':
                damage = skill_damage_formulas[skill] * 1
                return damage
            elif chosen_type == 'grass':
                damage = skill_damage_formulas[skill] * 1
                return damage
            elif chosen_type == 'water':
                damage = skill_damage_formulas[skill] * 1
                return damage
            else:
                damage = skill_damage_formulas[skill] * 1
                return damage
        elif creature['type'] == 'water':
            if chosen_type == 'normal':
                damage = skill_damage_formulas[skill] * 1
                return damage
            elif chosen_type == 'grass':
                damage = skill_damage_formulas[skill] * 2
                return damage
            elif chosen_type == 'water':
                damage = skill_damage_formulas[skill] * 0.5
                return damage
            else:
                damage = skill_damage_formulas[skill] * -0.5
                return damage
        else:
            if chosen_type == 'normal':
                damage = skill_damage_formulas[skill] * 1
                return damage
            elif chosen_type == 'grass':
                damage = skill_damage_formulas[skill] * -0.5
                return damage
            elif chosen_type == 'water':
                damage = skill_damage_formulas[skill] * 2
                return damage
            else:
                damage = skill_damage_formulas[skill] * 0.5
                return damage
    else:
        print("Unknown skill")
        return 0


def choose_skill(character):
    print("Available skills:")
    skills_list = list(character['skills'].keys())  # Convert skill names to a list
    for i in range(len(skills_list)):
        print(f"{i + 1}. {skills_list[i]}")

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


def drink_potion(character):
    if character['potion'] > 0:
        character['hp'] = character['max_hp']
        print("Your hp is full now!")
    else:
        print("You don't have potion...")


def engage_combat(character, creature):
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


def is_alive(character):
    return False if character["hp"] <= 0 else True


def handle_encounter(character, board):
    x, y = character['location']['x-coordinate'], character['location']['y-coordinate']
    current_location_type = board[(x, y)].split()[0]

    if current_location_type in ['Forest', 'Desert', 'Castle']:
        if random.random() < 0.8:  # 80% chance of encounter
            creature = create_creature(current_location_type)
            print(f"You've encountered a {creature['name']}!")
            print(f"The {creature['name']} is {creature['type']} type")
            # Offer choice to engage in combat or try to run
            action = input("Do you wish to fight (f) or try to run (r)? ")

            if action.lower() == 'f':
                engage_combat(character, creature)

                # Check if the character is alive after combat
                if character['hp'] <= 0:
                    print("You've been defeated. Game Over.")
                    return False  # This exits the function, potentially ending the game or requiring a game reset

                elif creature['health'] <= 0:
                    gained_exp = creature['exp']  # Use the creature's exp value
                    character['exp'] += gained_exp
                    print(f"You gained {gained_exp} Exp!")
                    character["money"] += creature["golds"]  # Add creature's gold
                    print(f"You got {creature['golds']} golds")
                    character_functions.update_level(character)  # Check and handle level up

            elif action.lower() == 'r':
                if random.random() < 0.5:  # 50% chance to escape
                    print("You managed to escape safely.")
                else:
                    print("Failed to escape. Forced into combat.")
                    engage_combat(character, creature)
            else:
                print("Invalid action. You're forced into combat.")
                engage_combat(character, creature)
        else:
            print("It's quiet... too quiet.")
