import random
import character_functions


def create_creature(region):
    # Define basic attributes for creatures in each region
    creatures = {
        'Forest': [
            {'name': 'Rabbit', 'health': 10, 'damage': 5, 'exp': 10},
            {'name': 'Gump', 'health': 20, 'damage': 10, 'exp': 15},
            {'name': 'Stump', 'health': 30, 'damage': 15, 'exp': 20},
            {'name': 'Nidalee', 'health': 50, 'damage': 20, 'exp': 30},
        ],
        'Desert': [
            {'name': 'Dune', 'health': 100, 'damage': 30, 'exp': 80},
            {'name': 'Scorpion', 'health': 200, 'damage': 50, 'exp': 100},
            {'name': 'Salamanders', 'health': 300, 'damage': 70, 'exp': 150},
            {'name': 'Sand Serpent', 'health': 500, 'damage': 100, 'exp': 250},

        ],
        'Castle': [
            {'name': 'Cerberus', 'health': 700, 'damage': 200, 'exp': 500},
            {'name': 'Gargoyle', 'health': 1000, 'damage': 300, 'exp': 800},
            {'name': 'Death Knight', 'health': 1500, 'damage': 500, 'exp': 1000},
            {'name': 'Lich', 'health': 2000, 'damage': 700, 'exp': 1500},
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


def calculate_skill_damage(skill, character):
    skill_damage_formulas = {
        'Shield Attack': character['stats']['str'] * 1.5 + character['stats']['dex'] * 2,
        'Power Strike': character['stats']['str'] * 2 + character['stats']['dex'] * 1,

        'Quick Shot': character['stats']['dex'] * 3 + character['stats']['str'] * 1,
        'Fire Arrow': character['stats']['dex'] * 3 + character['stats']['str'] * 2,

        'Fireball': character['stats']['int'] * 4,
        'Ice Age': character['stats']['int'] * 4 + character['stats']['dex'] * 2
    }
    if skill in skill_damage_formulas:
        damage = skill_damage_formulas[skill]
        return damage
    else:
        print("Unknown skill")
        return 0


def choose_skill(character):
    print("Available skills:")
    skill_number = 1  # Start numbering skills at 1
    for skill in character['skills']:
        print(f"{skill_number}. {skill}")
        skill_number += 1  # Increment the skill number for the next skill

    skill_choice = 0
    while skill_choice < 1 or skill_choice > len(character['skills']):
        try:
            skill_choice = int(input("Choose a skill to use (number): "))
        except ValueError:
            print("Please enter a number.")
    return character['skills'][skill_choice - 1]


def engage_combat(character, creature):
    print(f"Engaging in combat with {creature['name']}...")

    while creature['health'] > 0:
        # Let the user choose a skill
        chosen_skill = choose_skill(character)
        damage_dealt = calculate_skill_damage(chosen_skill, character)

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
    else:
        print("You move safely.")
