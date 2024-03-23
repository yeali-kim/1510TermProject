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
        'location': {'x-coordinate': 3, 'y-coordinate': 2},  # Default location at home
        'level': 1,  # Starting level
        'exp': 0,  # Starting experience points
        'skills': classes[character_class]['skills']  # Initial skills based on class
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


def game_loop():
    board = create_board_dict()
    character = create_character()  # Assume this function is adjusted to initialize a character without input prompts

    while True:
        print_board_dict(board)  # Optional: Customize to show character position
        print(f"Your location: {character['location']}")
        direction = get_user_choice()
        if direction == 'quit':
            break
        move_character(character, direction, board)


game_loop()

# Create a character by asking the user to choose a class
# character = create_character()
# print(character)
#
# board = create_board_dict()
# print_board_dict(board)
