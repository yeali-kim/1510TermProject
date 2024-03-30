import character_functions
import board
import combat


def game_loop():
    game_board = board.create_board()  # Create the game board
    character = character_functions.create_character()  # Create the character based on user input
    game_board = board.set_npc_location(game_board, character)  # Set the locations of NPCs on the board
    character["name"] = input("What is your name? ")
    print(f"\nWelcome to the adventure {character['name']}! Explore, fight creatures.\n")
    board.print_board(game_board, character)  # Display the game board
    
    while combat.is_alive(character):

        # Display character's current status
        print(f"\nCurrent location: ({character['location']['x-coordinate']}, {character['location']['y-coordinate']})")
        print(f"HP: {character['hp']} | Level: {character['level']} | Exp: {character['exp']}\n")
        print(f"Your stats: {character['stats']}, You have {character['money']} golds"
              f" and {character['elixir']} elixirs")

        direction = character_functions.get_user_choice()  # Get user input for the next action
        if direction == 'quit':
            print("Thank you for playing! Goodbye.")
            break
        if direction == 'elixir':
            combat.drink_elixir(character)
        character_functions.move_character(character, direction, game_board)  # Move the character based on the input
        heca_found(character, game_board)
        board.print_board(game_board, character)  # Display the game board

        combat.handle_encounter(character, game_board)  # Check for and handle any encounters


def main():
    game_loop()


if __name__ == "__main__":
    main()
