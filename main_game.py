import character_functions
import board
import combat
import npc


def game_loop():
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
    game_loop()


if __name__ == "__main__":
    main()
