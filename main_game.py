import character_functions
import board
import combat
import npc


def game_loop():
    """
    Run the main game loop. This function initializes the game state, handles player input, and updates the game
    based on the player's actions and game events. The game continues until the player's character dies or achieves
    the game objective.

    :precondition: all necessary modules (`board`, `character_functions`, `combat`, `npc`) are correctly implemented
    and available for creating the game board, character, handling movement, combat, and NPC interactions.
    :precondition: the game's environment and initial settings are predefined.
    :postcondition: updates the game board and character's state based on player actions and interactions.
    :postcondition: prints messages to guide the player through the game, including narrative introductions,
    status updates, and results of actions.
    :postcondition: the function ends when the player's character meets the game-ending conditions such as death or
    completing the main objective.
    """
    game_board = board.create_board()  # Create the game board
    character = character_functions.create_character()  # Create the character based on user input
    game_board = board.set_npc_location(game_board, character)  # Set the locations of NPCs on the board
    print("In a realm where legends breathe, the land of Dragon Coast calls for a hero to rise. You, the chosen one,\n"
          "embark on a quest to save the world from the Dragon Chris, a beast said to darken the skies and threaten "
          "all life.")
    character["name"] = input("Elder: Oh brave one, please tell me your name. ")
    print(f"Elder: {character['name']} please save us from Chris! But... do tread carefully. Not all is as it seems.")
    print(f"{character['name']}: Fear not, I shall bring peace back to Dragon Coast.")
    board.print_board(game_board, character)  # Display the game board
    
    while combat.is_alive(character) and npc.game_clear(character):
        # Display character's current status
        print(f"\nCurrent location: ({character['location']['x-coordinate']}, {character['location']['y-coordinate']})")
        print(f"HP: {character['hp']} | Level: {character['level']} | Exp: {character['exp']}\n")
        print(f"You have {character['money']} golds and {character['elixir']} elixirs")
        print(f"Your stats: str: {character['stats'][0]}, dex: {character['stats'][1]}, int: {character['stats'][2]}")

        direction = character_functions.get_user_choice()  # Get user input for the next action
        if direction == 'quit':
            print("Thank you for playing! Goodbye.")
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
