import random


def create_board() -> dict[tuple[int, int], str]:
    """
    Make game board.
    
    :return: a dictionary with coordinates as keys and values as the cell description
    >>> create_board()
    {(0, 0): 'School', (1, 0): 'School', (2, 0): 'School', (3, 0): 'vertical_wall', (4, 0): 'Town', (5, 0): 'Town',\
 (6, 0): 'Town', (7, 0): 'vertical_wall', (8, 0): 'Forest', (9, 0): 'Forest', (10, 0): 'Forest', (0, 1): 'School',\
 (1, 1): 'School', (2, 1): 'School', (3, 1): 'vertical_wall', (4, 1): 'Town', (5, 1): 'Town', (6, 1): 'Town',\
 (7, 1): 'Door to Forest', (8, 1): 'Forest', (9, 1): 'Forest', (10, 1): 'Forest', (0, 2): 'School',\
 (1, 2): 'School', (2, 2): 'School', (3, 2): 'vertical_wall', (4, 2): 'Town', (5, 2): 'Town', (6, 2): 'Town',\
 (7, 2): 'vertical_wall', (8, 2): 'Forest', (9, 2): 'Forest', (10, 2): 'Forest', (0, 3): 'School', (1, 3): 'School',\
 (2, 3): 'School', (3, 3): 'Door to School', (4, 3): 'Town', (5, 3): 'Town', (6, 3): 'Town',\
 (7, 3): 'vertical_wall', (8, 3): 'Forest', (9, 3): 'Forest', (10, 3): 'Forest', (0, 4): 'School', (1, 4): 'School',\
 (2, 4): 'School', (3, 4): 'vertical_wall', (4, 4): 'Town', (5, 4): 'Town', (6, 4): 'Town', (7, 4): 'vertical_wall',\
 (8, 4): 'Forest', (9, 4): 'Forest', (10, 4): 'Forest', (0, 5): 'horizontal_wall', (1, 5): 'horizontal_wall',\
 (2, 5): 'horizontal_wall', (3, 5): 'horizontal_wall', (4, 5): 'Door to Desert', (5, 5): 'horizontal_wall',\
 (6, 5): 'horizontal_wall', (7, 5): 'Desert', (8, 5): 'Forest', (9, 5): 'Forest', (10, 5): 'Forest',\
 (0, 6): 'Desert', (1, 6): 'Desert', (2, 6): 'Desert', (3, 6): 'Desert', (4, 6): 'Desert', (5, 6): 'Desert',\
 (6, 6): 'Desert', (7, 6): 'Desert', (8, 6): 'Forest', (9, 6): 'Forest', (10, 6): 'Forest', (0, 7): 'Desert',\
 (1, 7): 'Desert', (2, 7): 'Desert', (3, 7): 'Desert', (4, 7): 'Desert', (5, 7): 'Desert', (6, 7): 'Desert',\
 (7, 7): 'Desert', (8, 7): 'Forest', (9, 7): 'Forest', (10, 7): 'Forest', (0, 8): 'Desert', (1, 8): 'Desert',\
 (2, 8): 'Desert', (3, 8): 'Desert', (4, 8): 'Desert', (5, 8): 'Desert', (6, 8): 'Castle', (7, 8): 'Castle',\
 (8, 8): 'Castle', (9, 8): 'Castle', (10, 8): 'Castle', (0, 9): 'Desert', (1, 9): 'Desert', (2, 9): 'Desert',\
 (3, 9): 'Desert', (4, 9): 'Desert', (5, 9): 'Desert', (6, 9): 'Castle', (7, 9): 'Castle', (8, 9): 'Castle',\
 (9, 9): 'Castle', (10, 9): 'Castle', (0, 10): 'Desert', (1, 10): 'Desert', (2, 10): 'Desert', (3, 10): 'Desert',\
 (4, 10): 'Desert', (5, 10): 'Desert', (6, 10): 'Castle', (7, 10): 'Castle', (8, 10): 'Castle', (9, 10): 'Castle',\
 (10, 10): 'Castle'}
    """
    board = {}
    # Set fields on board
    for row in range(11):
        for col in range(11):
            board[(col, row)] = "Desert"
            if col in range(0, 3) and row in range(0, 5):
                board[(col, row)] = "School"
            elif col in range(4, 7) and row in range(0, 5):
                board[(col, row)] = "Town"
            elif col in range(8, 12) and row in range(0, 8):
                board[(col, row)] = "Forest"
            elif col in range(6, 12) and row in range(8, 11):
                board[(col, row)] = "Castle"
            if row == 5 and col < 7:
                board[(col, row)] = "horizontal_wall"
            if (col == 3 and row < 3 or col == 3 and row == 4 or col == 7 and row == 0 or
                    col == 7 and row == 2 or col == 7 and 1 < row < 5):
                board[(col, row)] = "vertical_wall"
    board[(3, 3)] = 'Door to School'  # Town to School
    board[(7, 1)] = 'Door to Forest'  # Town to Forest
    board[(4, 5)] = 'Door to Desert'  # Town to Desert
    return board


def set_npc_location(board: dict[tuple[int, int], str]) -> dict[tuple[int, int], str]:
    """
    Set the location of the NPCs on the board.
    
    :param board: a dictionary with coordinates as keys and cell description as values
    :return: a dictionary with coordinates as keys and the updated cell description as values
    """
    set_locations = {
        (0, 0): "jinkx",
        (0, 3): "chrissipus",
        (2, 2): "hypatia",
        (4, 1): "shawn",
        (6, 0): "david",
        (5, 4): "daniel",
        (6, 2): "home",
        (10, 10): "chris",
        (random.randint(0, 5), random.randint(7, 10)): "heca"
    }
    for location, value in set_locations.items():
        board[location] = value
    return board


def print_board(board: dict[tuple[int, int], str], character: dict[str, str | int | bool | dict[str, int]]):
    """
    Print board with given coordinates and descriptions.

    :param board: a dictionary with coordinates as keys and cell description as values
    :param character: a dictionary with attributes as keys and character description as values
    """
    print("╔═══" + "═══" * 2 + "═╦═" + "═══" * 3 + "═╦═" + "═══" * 3 + "╗")  # Top border
    for row in range(11):
        print("║", end="")  # Left border
        for col in range(11):
            cell_value = board[(col, row)]
            if (col, row) == (7, 5):
                print("═╝ ", end="")
            elif (col, row) == (3, 5):
                print("═╩═", end="")
            elif col == 11:
                if row != 5:
                    print("", end="")
            elif cell_value in ["jinkx", "chrissipus", "hypatia", "shawn", "david", "daniel"]:
                print("[*]", end="")
            elif cell_value == "home":
                print("[H]", end="")
            elif cell_value == "horizontal_wall":
                print("═══", end="")
            elif cell_value == "vertical_wall":
                print(" ║ ", end="")
            elif (col, row) == (character['location']['x-coordinate'], character['location']['y-coordinate']):
                print('\033[91m' + " P " + '\033[0m', end="")
            elif (col, row) in [(3, 3), (7, 1), (4, 5)]:
                print("   ", end="")
            elif cell_value == "Forest":
                print('\033[92m' + " ^ " + '\033[0m', end="")
            elif cell_value == "Desert" or cell_value == "heca":
                print('\033[93m' + " ~ " + '\033[0m', end="")
            elif cell_value == "Castle":
                print('\033[90m' + " # " + '\033[0m', end="")
            elif cell_value == "chris":
                print('\033[91m' + " @ " + '\033[0m', end="")
            else:
                print("   ", end="")
        print("║")  # Right border
    print("╚═══" + "═══" * 10 + "╝")  # Bottom border
    
