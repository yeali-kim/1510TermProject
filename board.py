import random


def create_board() -> dict[tuple[int, int], str]:
    """
    Make game board.
    
    :return: a dictionary with coordinates as keys and values as the cell description
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
    
