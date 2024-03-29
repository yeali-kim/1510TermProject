import random
import npc

def create_board():
    board = {}
    # Set fields on board
    for row in range(11):
        for col in range(11):
            board[(col, row)] = "Forest"
            if col in range(0, 3) and row in range(0, 5):
                board[(col, row)] = "School"
            elif col in range(4, 7) and row in range(0, 5):
                board[(col, row)] = "Town"
            elif col in range(8, 12) and row in range(0, 8):
                board[(col, row)] = "Desert"
            elif col in range(6, 12) and row in range(8, 11):
                board[(col, row)] = "Castle"
            if row == 5 and col < 7:
                board[(col, row)] = "horizontal_wall"
            if col == 3 and row < 3 or col == 3 and row == 4 or col == 7 and row == 0 or col == 7 and row == 2 or col == 7 and 1 < row < 5:
                board[(col, row)] = "vertical_wall"

    # Set NPC and home location
    set_locations = {
        (0, 0): npc.jinkx,
        (0, 3): npc.chrissipus,
        (2, 2): npc.hypatia,
        (4, 1): npc.shawn,
        (6, 0): npc.david,
        (5, 4): npc.daniel,
        (6, 2): "home",
        (10, 10): npc.chris,
        (random.randint(8, 11), random.randint(0, 8)): npc.daughter 
    }

    for location, value in set_locations.items():
        board[location] = value

    return board


def print_board(board, character):
    print("╔═══" + "═══" * 2 + "═╦═" + "═══" * 3 + "═╦═" + "═══" * 3 + "╗")  # Top border
    for row in range(11):
        print("║", end="")  # Left border
        for col in range(11):
            cell_value = board[(col, row)]
            if (col, row) == (7, 5):
                print("═╝ ", end="")
            elif (col, row) == (3, 5):
                print("═╩═", end="")
            elif (col, row) in [(3, 3), (7, 1), (4, 5)]:
                print("   ", end="")
            elif col == 11:
                if row != 5:
                    print("", end="")
            elif cell_value in [npc.jinkx, npc.chrissipus, npc.hypatia, npc.shawn, npc.david, npc.daniel, npc.chris, npc.daughter]:
                print("[*]", end="")
            elif cell_value == "home":
                print("[H]", end="")
            elif cell_value == "horizontal_wall":
                print("═══", end="")
            elif cell_value == "vertical_wall":
                print(" ║ ", end="")
            elif (col, row) == (character['location']['x-coordinate'], character['location']['y-coordinate']):
                print('\033[91m' + " P " + '\033[0m', end="")
            elif cell_value == "Desert":
                print('\033[92m' + " ^ " + '\033[0m', end="")
            elif cell_value == "Forest":
                print('\033[93m' + " ~ " + '\033[0m', end="")
            elif cell_value == "Castle":
                print('\033[90m' + " # " + '\033[0m', end="")
            elif cell_value == "dragon":
                print('\033[91m' + " @ " + '\033[0m', end="")
            else:
                print("   ", end="")
        print("║")  # Right border
    print("╚═══" + "═══" * 10 + "╝")  # Bottom border
    
