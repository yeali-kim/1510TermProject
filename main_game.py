import character_functions
import board
import combat


def game_loop():
    game_board = board.create_board()  # Create the game board
    character = character_functions.create_character()  # Create the character based on user input

    print("\nWelcome to the adventure! Explore, fight creatures, and discover treasures.\n")
    while combat.is_alive(character):
        board.print_board(game_board, character)  # Display the game board

        # Display character's current status
        print(f"\nCurrent location: ({character['location']['x-coordinate']}, {character['location']['y-coordinate']})")
        print(f"HP: {character['hp']} | Level: {character['level']} | Exp: {character['exp']}\n")

        direction = character_functions.get_user_choice()  # Get user input for the next action
        if direction == 'quit':
            print("Thank you for playing! Goodbye.")
            break
        
        character_functions.move_character(character, direction, game_board)  # Move the character based on the input
        combat.handle_encounter(character, game_board)  # Check for and handle any encounters
        


def main():
    game_loop()
    


if __name__ == "__main__":
    main()
