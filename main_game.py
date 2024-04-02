import character_functions
import board
import combat
import npc
import time


def game_loop():
    """
    Run the main game loop. This function initializes the game state, handles player input, and updates the game
    based on the player's actions and game events. The game continues until the player's character dies or achieves
    the game objective.

    :precondition: all necessary modules (`board`, `character_functions`, `combat`, `npc`) are correctly implemented
    and available for creating the game board, character, handling movement, combat, and NPC interactions.
    :precondition: the game's environment and initial settings are predefined.
    :postcondition: update the game board and character's state based on player actions and interactions.
    :postcondition: print messages to guide the player through the game, including narrative introductions,
    status updates, and results of actions.
    :postcondition: the function ends when the player's character meets the game-ending conditions such as death or
    completing the main objective.
    """
    game_board = board.create_board()  # Create the game board
    character = character_functions.create_character()  # Create the character based on user input
    game_board = board.set_npc_location(game_board)  # Set the locations of NPCs on the board
    greet_texts = [
        "In a realm where legends breathe, the land of Dragon Coast calls for a hero to rise.",
        "You, the chosen one, embark on a quest to save the world from the Dragon \033[0;31mChris\033[0m,",
        "a beast said to darken the skies and threaten all life."
        ]
    chris_face = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠉⠁⠀⠀⡜⠀⠀⠀⠀⣠⠔⠋⠉⠀⠀⠀⠀⠀⠀⠀⡠⠊
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠉⠀⠀⠀⠀⢀⡜⠁⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠛⣆⠀⠀⠀⠀⠀⣠⠾⢒⡶⠊⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣁⡀⠈⠉⠁⠒⢒⣾⡽⡖⠉⠀⠀⠀⢠⠂⠀⠀⠀⣠⠞⠧⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠉⢉⣀⠀⠀⠀⣠⠞⠉⠀⠀⠘⢄⠀⠀⠀⡈⠀⠀⣠⠞⠁⠀⠀⠀⠉⠳⢤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣏⡤⠊⠁⠀⡠⠚⡿⠁⠀⣀⡾⣥⠄⠀⠀⠀⠀⠀⠉⠢⣞⣁⣀⣴⡃⠀⠀⠀⠀⠀⠀⣀⡠⠽⠒⠊
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠋⠀⠀⢠⠞⠀⠀⠓⠒⠉⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣁⣀⠤⠴⠒⠚⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⡀⠀⠀⡠⠚⠁⠀⠀⠀⠀⠀⠀⡘⠁⠀⠀⠀⢠⠇⠀⢀⠀⢀⡠⠔⠋⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠋⠀⢠⠎⠀⠀⠀⠀⠀⠀⣀⡤⠚⠀⠀⠀⠀⠀⣿⠒⠀⠀⠳⣄⠀⠀⠀⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡎⠀⠀⠀⣠⣶⣾⡿⣿⢠⠃⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠘⡆⠀⠀⠈⢇⠀⠀⠀⠀⢀⡠⠔⠊⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠇⠀⠀⣰⣿⣇⣳⣧⠟⠃⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⢰⠇⠀⠀⠀⠘⢄⡠⠔⠪⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠀⢰⠋⠀⠀⠀⠀⠀⠀⠐⠉⠉⢩⠟⠁⠀⠀⢠⠶⠒⡖⢲⠏⠀⠀⠀⠀⠀⢸⠤⠔⢆⠀⠀⢨⠇⠀⠀⠙⢄⠀⠀⠀⠀⠀
⠀⠀⠀⡼⢹⣔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⢠⣟⢢⠀⢸⠎⠀⠀⠀⠀⠀⠀⡎⠀⣀⡬⠗⠶⣋⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀
⠀⣠⠚⡇⣀⡼⠁⠀⠀⠀⠀⠀⣠⠤⠀⠀⠘⠀⠀⠀⣠⠏⠀⡄⢳⡞⠀⠀⠀⠀⠀⠀⢰⡇⡘⠁⠀⠀⠀⠈⠣⡀⠀⠀⠀⠀⠱⡄⠀⠀
⢠⠇⠀⠈⠀⠀⣠⠆⠀⠀⢀⠞⢁⣤⣤⣤⠤⠤⠖⠚⠻⢶⣄⠰⣰⠃⠀⠀⠀⠀⠀⠀⢸⠁⠇⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⠘⡄⠀
⠸⡄⠀⠀⠀⠐⠁⠀⠀⠀⣠⣶⢿⣍⡿⣏⣀⡤⠤⠒⠒⠒⠈⠹⣿⠀⠀⠀⠀⠀⠀⠀⢘⣿⠤⠤⠔⠒⠒⠒⠒⠤⢼⠄⠀⠀⠀⠀⠸⡀
⠀⠙⢦⣄⣀⣀⣀⣀⣤⣾⠛⢟⠺⠆⣰⠞⠁⠀⠀⠀⠀⣀⣀⣀⡿⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱
⠀⠀⠀⠘⣿⣿⣿⣽⣧⣿⠢⡘⡄⢰⠃⠀⠀⠀⢀⡤⠤⠤⠄⢼⣇⠀⠀⠀⠀⢀⠞⠁⠉⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠉⠈⡇⠀⠀⠀⡿⡅⠀⠀⢀⣸⣿⠀⠀⠀⡴⠋⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⢀⣴⣷⣷⠀⠀⣸⣍⡏⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠖⠚⣋⡡⠔⠋⠀⢈⣿⠀⢀⣛⣼⡇⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⣺⠭⠔⠒⠊⣉⡇⠀⠀⣄⣠⣾⣿⠄⣀⢫⡽⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣏⠻⣀⣀⣀⣤⡾⠋⡀⠀⠀⠙⣏⡿⣬⣦⣀⡽⠁⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⢱⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠦⠤⠤⠭⠽⠟⠋⠁⠀⠀⠀⠹⢍⡉⠉⠁⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀"""
    for text in greet_texts:
        print(text)
        time.sleep(2)
    lines = chris_face.split("\n")
    for line in lines:
        print("\033[0;31m" + line + "\033[0m")  # Print the face of the dragon Chris in red
        time.sleep(0.1)
    name = input("\033[0;34mElder\033[0m: Oh brave one, please tell me your name.") # Get the player's name
    time.sleep(1)
    while not name:
        name = input("\033[0;34mElder\033[0m: I apologize, but I must ask again. What is your name?")
    character["name"] = name
    start_texts = [
        f"\033[0;34mElder\033[0m: \033[1;33m{character['name']}\033[0m, please save us from \033[0;31mChris\033[0m!",
        "But... do tread carefully. Not all is as it seems.",
        f"\033[1;33m{character['name']}\033[0m: Fear not, I shall bring peace back to Dragon Coast.",
        ".",
        ".",
        ".",
        "And so, the journey begins..."
        ]
    for text in start_texts:
        print(text)
        time.sleep(1)

    board.print_board(game_board, character)  # Display the game board
    while combat.is_alive(character) and npc.game_clear(character):
        # Display character's current status
        print(f"\nCurrent location: ({character['location']['x-coordinate']}, {character['location']['y-coordinate']})")
        print(f"HP: {character['hp']} | Level: {character['level']} | Exp: {character['exp']}\n")
        print(f"You have {character['gold']} gold and {character['elixir']} elixir(s)")
        print(f"Your stats: str: {character['stats'][0]}, dex: {character['stats'][1]}, int: {character['stats'][2]}")

        direction = character_functions.get_user_choice()  # Get user input for the next action
        if direction == 'quit':
            print("Thank you for playing, \033[1;33m{character['name']}\033[0m! Goodbye.")
            break
        if direction == 'elixir':
            combat.drink_elixir(character)
        character_functions.move_character(character, direction, game_board)  # Move the character based on the input
        npc.heca_found(character, game_board)
        board.print_board(game_board, character)  # Display the game board
        combat.handle_encounter(character, game_board)  # Check for and handle any encounters
    print(f"{character['name']} is {character['class']}, has {character['skills']} skills")


def main():
    """
    Drive the program.
    """
    game_loop()


if __name__ == "__main__":
    main()
