import character_functions
import board
import combat
import npc
import time


def game_loop():
    game_board = board.create_board()  # Create the game board
    character = character_functions.create_character()  # Create the character based on user input
    game_board = board.set_npc_location(game_board, character)  # Set the locations of NPCs on the board
    greet_art = r"""\    .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
 """
    lines = greet_art.split('\n')

    for line in lines:
        print(line)
        time.sleep(0.2)
    
    welcome_messages = [
        "Welcome to Thompsonville!",
        "Thompsonville is a small town surrounded by a forest and a desert.",
        "You are a brave adventurer who has come to Thompsonville to explore and fight creatures.",
        "You can move around the town and explore the forest and desert.",
        "You will encounter creatures and NPCs on your journey.",
        "You can fight creatures to gain experience and gold.",
        "You can also interact with town NPCs to get quests and rewards.",
    ]
    for message in welcome_messages:
        print(message)
        time.sleep(1.5)
    name = input("Before we get started, what's your name?: ")
    while not name:
        name = input("Invalid entry. Please enter your name: ")
    character['name'] = name          
    guide_messages = [
        "Welcome, adventurer \u001b[33;1m{character['name']}\033[0m!",
        "You are currently at your home in the town of Thompsonville.",
        "You can move by typing 'up', 'down', 'left', or 'right'.",
        "You can also type 'quit' to exit the game at any time.",
        "First, let's head to the school to get you some basic training!",
    ]
    for message in guide_messages:
        print(message)
        time.sleep(1.5)
    board.print_board(game_board, character)  # Display the game board
    time.sleep(0.5)
    while combat.is_alive(character):
        # Display character's current status
        print(f"\nCurrent location: ({character['location']['x-coordinate']}, {character['location']['y-coordinate']})")
        print(f"HP: {character['hp']} | Level: {character['level']} | Exp: {character['exp']}\n")
        print(f"Your stats: {character['stats']}, You have {character['money']} golds"
              f" and {character['elixir']} elixirs")
        print(f"Your stats: str: {character['stats'][0]}, dex: {character['stats'][1]}, int: {character['stats'][2]}"
              f" You have {character['money']} golds"
              f" and {character['elixir']} elixirs")

        direction = character_functions.get_user_choice()  # Get user input for the next action
        if direction == 'quit':
            print("Thank you for playing, \u001b[33;1m{character['name']}\033[0m! Goodbye.")
            break
        if direction == 'elixir':
            combat.drink_elixir(character)
        character_functions.move_character(character, direction, game_board)  # Move the character based on the input
        npc.heca_found(character, game_board)
        board.print_board(game_board, character)  # Display the game board

        combat.handle_encounter(character, game_board)  # Check for and handle any encounters


def main():
    game_loop()


if __name__ == "__main__":
    main()
