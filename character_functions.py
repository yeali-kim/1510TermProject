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
        'Knight': {'str': 10, 'dex': 5, 'int': 2, 'hp': 150, 'max_hp': 150, 'skills': ['Shield Attack', 'Power Strike']},
        'Archer': {'str': 6, 'dex': 10, 'int': 3, 'hp': 100, 'max_hp': 100, 'skills': ['Quick Shot', 'Fire Arrow']},
        'Magician': {'str': 3, 'dex': 4, 'int': 10000, 'hp': 80, 'max_hp':80, 'skills': ['Fireball', 'Ice Age']},
    }

    # Initialize the character with class-specific stats, location, level, Exp, and skills
    user_character = {
        'class': character_class,
        'stats': classes[character_class],
        'location': {'x-coordinate': 6, 'y-coordinate': 2},  # Default location at home
        'level': 1,  # Starting level
        'exp': 0,  # Starting experience points
        'skills': classes[character_class]['skills'],  # Initial skills based on class
        'hp': classes[character_class]['hp'],
    }

    return user_character


def update_level(character):
    # Base experience required for the first level up
    base_exp_per_level = 100
    # Experience growth rate for each subsequent level
    exp_growth_rate = 1.05  # 5% more Exp required for each level
    # base hp to calculate total hp when character leveled up
    base_hp = {
        'Knight': 150,
        'Archer': 100,
        'Magician': 80,
    }

    # Calculate the current required Exp for the next level
    exp_for_next_level = base_exp_per_level * (exp_growth_rate ** (character['level'] - 1))

    # Check if the character has enough Exp to level up
    if character['exp'] >= exp_for_next_level:
        character['exp'] -= exp_for_next_level  # Deduct the Exp used to level up
        character['level'] += 1  # Increase level

        # Print level-up message
        print(f"Congratulations! Your character is now level {character['level']}.")

        # Stat increases depend on character class
        if character['class'] == 'Knight':  # Knight get more hp than other classes
            character['stats']['str'] += 2
            character['stats']['dex'] += 1
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level']-1)/10)), 0)  # 10% increase hp
            character['hp'] = character['max_hp']
        elif character['class'] == 'Archer':
            character['stats']['str'] += 1
            character['stats']['dex'] += 3
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level']-1)/10)), 0)  # 10% increase hp
            character['hp'] = character['max_hp']
        elif character['class'] == 'Magician':
            character['stats']['dex'] += 2
            character['stats']['int'] += 3
            character['max_hp'] = round(base_hp[character['class']] * (1 + ((character['level']-1)/10)), 0)  # 10% increase hp
            character['hp'] = character['max_hp']

        print("Your stats have increased:")
        print(f"Strength: {character['stats']['str']}, Dexterity: {character['stats']['dex']}, \
        Intelligence: {character['stats']['int']}, HP: {character['hp']}")

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
    if board[(new_x, new_y)] != 'horizontal_wall' or 'vertical_wall':
        if "Door" in board[(new_x, new_y)]:
            print(f"Moving through the door to {board[(new_x, new_y)]}...")
        character['location']['x-coordinate'], character['location']['y-coordinate'] = new_x, new_y
    else:
        print("Invalid move. You've hit a wall.")