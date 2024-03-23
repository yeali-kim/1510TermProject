import random


def create_board_dict():
    # Initialize the board as a dictionary
    board = {(x, y): ' ' for x in range(10) for y in range(10)}

    # School
    for x in range(2):
        for y in range(5):
            board[(x, y)] = 'School'
    school_npcs = [(0, 1), (1, 2), (0, 3)]
    for npc in school_npcs:
        board[npc] = 'NPC skill ' + str(school_npcs.index(npc) + 1)

    # Town
    for x in range(2, 6):
        for y in range(5):
            board[(x, y)] = 'Town'
    board[(4, 2)] = 'Home'
    town_npcs = [(3, 0), (3, 3), (4, 1), (5, 3), (3, 4)]
    for npc in town_npcs:
        board[npc] = 'NPC'

    # Forest
    for x in range(6, 10):
        for y in range(5):
            board[(x, y)] = 'Forest'
    forest_npc = (random.randint(6, 9), random.randint(0, 4))
    board[forest_npc] = 'NPC'

    # Desert
    for x in range(6):
        for y in range(5, 10):
            board[(x, y)] = 'Desert'
    desert_npc = (random.randint(0, 5), random.randint(5, 9))
    board[desert_npc] = 'NPC'

    # Castle
    for x in range(6, 10):
        for y in range(5, 10):
            board[(x, y)] = 'Castle'
    board[(9, 9)] = 'Boss'

    wall_locations = [(6, i) for i in range(10)]
    wall_locations += [(i, 5) for i in range(10)]
    wall_locations += [(2, i) for i in range(5)]
    for wall in wall_locations:
        board[wall] = 'Wall'

    # Doors - Placed based on the transition areas
    board[(2, 4)] = 'Door to Town'  # School to Town
    board[(6, 2)] = 'Door to Forest'  # Town to Forest
    board[(4, 5)] = 'Door to Desert'  # Town to Desert
    board[(6, 8)] = 'Door to Castle'  # Desert to Castle

    return board


def print_board_dict(board):
    for y in range(10):
        row = [board[(x, y)] for x in range(10)]
        print('         '.join(row))
        print("")


def create_character():
    # Mapping of input numbers to character classes
    class_options = {1: 'Knight', 2: 'Archer', 3: 'Magician'}
    character_class = None
    base_hp = {
        'Knight': 150,
        'Archer': 100,
        'Magician': 80,
    }
    # Attempt to get user input and validate it
    while character_class is None:
        try:
            choice = int(input("Enter the number that you want for your class - 1. Knight, 2. Archer, 3. Magician: "))
            if choice in class_options:
                character_class = class_options[choice]
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number to choose your class!")

    # Define default stats for each class
    classes = {
        'Knight': {'str': 10, 'dex': 5, 'int': 2, 'skills': ['Shield Attack', 'Power Strike']},
        'Archer': {'str': 6, 'dex': 10, 'int': 3, 'skills': ['Quick Shot', 'Fire Arrow']},
        'Magician': {'str': 3, 'dex': 4, 'int': 10, 'skills': ['Fireball', 'Ice Age']},
    }

    # Initialize the character with class-specific stats, location, level, Exp, and skills
    user_character = {
        'class': character_class,
        'stats': classes[character_class],
        'location': {'x-coordinate': 4, 'y-coordinate': 2},  # Default location at home
        'level': 1,  # Starting level
        'exp': 0,  # Starting experience points
        'skills': classes[character_class]['skills'],  # Initial skills based on class
        'hp': base_hp[character_class],
    }

    return user_character


def update_level(character):
    # Base experience required for the first level up
    base_exp_per_level = 100
    # Experience growth rate for each subsequent level
    exp_growth_rate = 1.2  # 20% more Exp required for each level

    # Calculate the current required Exp for the next level
    exp_for_next_level = base_exp_per_level * (exp_growth_rate ** (character['level'] - 1))

    # Check if the character has enough Exp to level up
    if character['exp'] >= exp_for_next_level:
        character['exp'] -= exp_for_next_level  # Deduct the Exp used to level up
        character['level'] += 1  # Increase level

        # Print level-up message
        print(f"Congratulations! Your character is now level {character['level']}.")

        # Stat increases depend on character class
        if character['class'] == 'Knight':
            character['stats']['str'] += 2  # Knights get stronger
            character['stats']['dex'] += 1  # Minor dexterity increase
        elif character['class'] == 'Archer':
            character['stats']['str'] += 1
            character['stats']['dex'] += 2  # Archers become more dexterous
        elif character['class'] == 'Magician':
            character['stats']['dex'] += 1
            character['stats']['int'] += 2  # Magicians' intelligence greatly increases

        # Print stat increase message
        print("Your stats have increased:")
        print(f"Strength: {character['stats']['str']}, Dexterity: {character['stats']['dex']}, \
        Intelligence: {character['stats']['int']}")

        # Check for another level up in case of remaining Exp
        update_level(character)
    else:
        print(f"You need {exp_for_next_level - character['exp']} more Exp to reach level {character['level'] + 1}.")


def get_user_choice():
    user_input = ""
    while user_input not in ["up", "down", "left", "right", "quit"]:
        user_input = input("Enter movement direction (up, down, left, right) or 'quit' to exit: ")
        user_input = user_input.lower()
    return user_input


def move_character(character, direction, board):
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

    # Determine if the new location is an NPC
    if "NPC" in board[(new_x, new_y)]:
        print(f"Encountered {board[(new_x, new_y)]}. Interaction not yet implemented.")

    # Allow movement if it's within the same region, through a door, or from home
    if board[(new_x, new_y)] != 'Wall':
        if "Door" in board[(new_x, new_y)]:
            print(f"Moving through the door to {board[(new_x, new_y)]}...")
        character['location']['x-coordinate'], character['location']['y-coordinate'] = new_x, new_y
    else:
        print("Invalid move. You've hit a wall.")


def handle_encounter(character, board):
    x, y = character['location']['x-coordinate'], character['location']['y-coordinate']
    current_location_type = board[(x, y)].split()[0]

    if current_location_type in ['Forest', 'Desert']:
        if random.random() < 0.8:  # 30% chance of encounter
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
                    update_level(character)  # Check and handle level up

            elif action.lower() == 'r':
                # Implement escape logic, could be based on character's dex vs creature's dex
                # Simple escape chance demonstration
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


def create_creature(region):
    # Define basic attributes for creatures in each region
    creatures = {
        'Forest': [
            {'name': 'Rabbit', 'health': 10, 'damage': 5, 'exp': 10},
            {'name': 'Wolf', 'health': 20, 'damage': 10, 'exp': 20},
            {'name': 'Bear', 'health': 50, 'damage': 20, 'exp': 30},
        ],
        'Desert': [
            {'name': 'Scorpion', 'health': 200, 'damage': 500, 'exp': 100},
            {'name': 'Sand Serpent', 'health': 500, 'damage': 100, 'exp': 250},
        ],
    }

    if region in creatures:
        # Randomly select a creature from the specified region
        creature = random.choice(creatures[region])
        print(f"A wild {creature['name']} appears!")
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
            if skill_choice < 1 or skill_choice > len(character['skills']):
                print("Invalid choice, please select a valid skill number.")
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


def game_loop():
    board = create_board_dict()  # Initialize the game board
    character = create_character()  # Create the character based on user input

    print("\nWelcome to the adventure! Explore, fight creatures, and discover treasures.\n")

    while is_alive(character):
        print_board_dict(board)  # Display the game board

        # Display character's current status
        print(f"\nCurrent location: ({character['location']['x-coordinate']}, {character['location']['y-coordinate']})")
        print(f"HP: {character['hp']} | Level: {character['level']} | Exp: {character['exp']}\n")

        direction = get_user_choice()  # Get user input for the next action
        if direction == 'quit':
            print("Thank you for playing! Goodbye.")
            break

        move_character(character, direction, board)  # Move the character based on the input
        handle_encounter(character, board)  # Check for and handle any encounters


def main():
    game_loop()


if __name__ == "__main__":
    main()
