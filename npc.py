import time
import character_functions
import random
import combat


def jinkx(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Offers the player's character an opportunity to learn magic and become a 'Magician'
    if they are currently a 'Citizen'.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must contain a class key
    :precondition: the character's class must be Citizen for the class change to occur
    :postcondition: if the character is a Citizen and the player accepts Jinkx's offer, the character's class is
    changed to Magician and their skills are updated accordingly
    :postcondition: if the character is a Knight or an Archer, Jinkx responds differently, and no class change occurs
    :postcondition: if the character is a Citizen but the player refuses Jinkx's offer, no class change occurs
    """
    if character['class'] == 'Citizen':  # check if class is Citizen
        # ask user if they want to talk to Jinkx
        say_hi = input(
            "You met \033[1;35mJinkx\033[0m, the wise wizard. Do you want to talk to her? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            greet_lines = ["\033[1;35mJinkx\033[0m: Hi there little fella! My name is \033[1;35mJinkx\033[0m, the wise wizard!",
                           "I can teach you some magic spells.",
                           "If you learn from me, you will become the best magician in the world!"
                           "But you won't be able to choose other classes."]
            for line in greet_lines:
                print(line)
                time.sleep(1)
            user_action = input(
                "Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn magic spells
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mJinkx\033[0m: Wonderful! Let's start right away. Abracadabra!",
                "n": "\033[1;35mJinkx\033[0m: Fine. You don't look like a wizard material anyways."
            }
            if user_action == "y":
                character['class'] = 'Magician'  # set class to Magician
                character_functions.update_skills(character)  # update skills
                lines = [
                    responses["y"],
                    "...",
                    "...",
                    "Great job surviving through the training.",
                    "You are now a \033[92mMAGICIAN\033[0m!",
                    "Use your new skills wisely.\n",
                    f"\u001b[34mYour class is now \033[92m{character['class']}\033[0m.",
                    f"\u001b[34mNow you can use these skills. \033[92m{character['skills']}\033[0m."
                ]
                for line in lines:
                    print(line)
                    time.sleep(1)
            else:
                print(responses["n"])
                time.sleep(1)
    elif character['class'] == 'Knight':
        print("\033[1;35mJinkx\033[0m: You are already a knight. Chrissipus will be disappointed.")
    else:
        print("\033[1;35mJinkx\033[0m: You are already an archer. Hypatia will be disappointed.")


def chrissipus(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Offers the player's character an opportunity to learn chivalry and become a 'Knight'
    if they are currently a 'Citizen'.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must contain a class key
    :precondition: the character's class must be Citizen for the class change to occur
    :postcondition: if the character is a Citizen and the player accepts chrissipus' offer, the character's class is
    changed to Knight and their skills are updated accordingly
    :postcondition: if the character is a Magician or an Archer, chrissipus responds differently,
    and no class change occurs
    :postcondition: if the character is a Citizen but the player refuses chrissipus' offer, no class change occurs
    """
    if character['class'] == 'Citizen':  # check if class is Citizen
        say_hi = input(
            "You met \033[1;35mChrissipus\033[0m, the mighty knight. Do you want to talk to him? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            greet_lines = ["\033[1;35mChrissipus\033[0m : Hi there young man! My name is \033[1;35mChrissipus\033[0m, the mighty "
                "knight!"
                "I can teach you some sword skills.",
                "If you learn from me, you will become the best swordsman in the world!",
                "But you won't be able to choose other classes."]
            for line in greet_lines:
                print(line)
                time.sleep(1)
            user_action = input(
                "Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn sword skills
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mChrissipus\033[0m: I knew it! Grab your sword my friend! Not that one. That one is "
                     "expensive.",
                "n": "\033[1;35mChrissipus\033[0m: Fine. Pfft, look at your size anyways."
            }
            if user_action == "y":
                character['class'] = 'Knight'  # set class to Knight
                character_functions.update_skills(character)  # update skills
                lines = [
                    responses["y"],
                    "...",
                    "...",
                    "Great job surviving through the training.",
                    "You are now a \033[92mKNIGHT\033[0m!",
                    "Use your new skills carefully.\n",
                    f"\u001b[34mYour class is now \033[92m{character['class']}\033[0m.",
                    f"\u001b[34mNow you can use these skills. \033[92m{character['skills']}\033[0m."
                ]
                for line in lines:
                    print(line)
                    time.sleep(1)
            else:
                print(responses["n"])
                time.sleep(1)
    elif character['class'] == 'Magician':
        print("\033[1;35mChrissipus\033[0m: You are already a magician. Jinkx will be disappointed.")
    else:
        print("\033[1;35mChrissipus\033[0m: You are already an archer. Hypatia will be disappointed.")


def hypatia(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Offers the player's character an opportunity to learn detecting and become a 'Archer'
    if they are currently a 'Citizen'.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must contain a class key
    :precondition: the character's class must be Citizen for the class change to occur
    :postcondition: if the character is a Citizen and the player accepts hypatia's offer, the character's class is
    changed to Archer and their skills are updated accordingly
    :postcondition: if the character is a Magician or a Knight, hypatia responds differently and no class change occurs
    :postcondition: if the character is a Citizen but the player refuses hypatia's offer, no class change occurs
    """
    if character['class'] == 'Citizen':  # check if class is Citizen
        say_hi = input(
            "You met \033[1;35mHypatia\033[0m, the great archer. Do you want to talk to her? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            greet_lines = ["\033[1;35mHypatia\033[0m: Hi there young man! My name is \033[1;35mHypatia\033[0m, the great archer!",
                           "I can teach you some archery skills.",
                           "If you learn from me, you will become the best archer in the world!"
                           "But you won't be able to choose other classes."]
            for line in greet_lines:
                print(line)
                time.sleep(1)
            user_action = input(
                "Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn archery skills
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mHypatia\033[0m: I knew it! I will make you the best archer in the world!",
                "n": "\033[1;35mHypatia\033[0m: Fine. You look clumsy anyways. Archery is not for everyone."
            }
            if user_action == "y":
                character['class'] = 'Archer'  # set class to Archer
                character_functions.update_skills(character)  # update skills
                lines = [
                    responses["y"],
                    "...",
                    "...",
                    "Great job surviving through the training.",
                    "You are now an \033[92mARCHER\033[0m!",
                    "Use your new skills thoughtfully.\n",
                    f"\u001b[34mYour class is now \033[92m{character['class']}\033[0m.",
                    f"\u001b[34mNow you can use these skills. \033[92m{character['skills']}\033[0m."
                ]
                for line in lines:
                    print(line)
                    time.sleep(1)
            else:
                print(responses["n"])
                time.sleep(1)
    elif character['class'] == 'Magician':
        print("\033[1;35mHypatia\033[0m : You are already a magician. Jinkx will be disappointed.")
    else:
        print("\033[1;35mHypatia\033[0m : You are already a knight. Chrissipus will be disappointed.")


def shawn(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Initiates or updates the status of Shawn's quest based on the character's interaction and quest progress.

    :param character: a dictionary representing a character
    :precondition: the character dictionary must contain shawn_quest to indicate if shawn's quest has been accepted
    and heca_found to indicate if haca has been found
    :postcondition: if the user accepts shawn's quest, shawn_quest is set to True
    :postcondition: if the user has completed the quest by finding heca, shawn_quest is se to False,
    and the character is rewarded with elixirs
    :postcondition: function updates the character's state based on the quest's progress and the user's action
    during the encounter
    """
    if character["shawn_quest"] is None:
        say_hi = input(
            "You met \u001b[34;1mShawn\033[0m, the mayor. Do you want to talk to him? (Y/N): ").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N: ").strip().lower()
        if say_hi == "y":
            print(
                "\u001b[34;1mShawn\033[0m: Hello there! My name is \u001b[34;1mShawn\033[0m. "
                "Please, I need your help..")
            time.sleep(1)
            user_action = (input(
                "My daughter \u001b[36mHeca\033[0m has been missing for a month. Can you help me find her? (Y/N): ")
                           .strip().lower())
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N: ").strip().lower()
            responses = {
                "y": "\u001b[34;1mShawn\033[0m: Thank you so much! Please find my daughter. She was last seen in the "
                     "Desert.",
                "n": "\u001b[34;1mShawn\033[0m: I understand. It's a difficult task. I'll just keep waiting."
            }
            if user_action == "y":
                print(responses["y"])
                character["shawn_quest"] = True
            else:
                print(responses["n"])
    elif character["shawn_quest"] and character["heca_found"] is False:
        print(
            "\u001b[34;1mShawn\033[0m: I'm still waiting for you to find my daughter \u001b[36mHeca\033[0m. Please "
            "hurry.")
    elif character["shawn_quest"] and character["heca_found"]:
        character["elixir"] += 3
        character["shawn_quest"] = False
        print(
            "\u001b[34;1mShawn\033[0m: Thank you for finding my daughter \u001b[36mHeca\033[0m! I am forever grateful.")
        time.sleep(1)
        print("\u001b[34;1mShawn\033[0m: Please take these elixirs as a token of my gratitude.")
        time.sleep(1)
        print("You received \u001b[37;1m3 \u001b[37melixirs\033[0m.")
        time.sleep(1)
        print(f"You now have \u001b[37;1m{character["elixir"]} \u001b[37melixirs\033[0m.")
    else:
        print(
            "\u001b[34;1mShawn\033[0m: Thank you for finding my daughter \u001b[36mHeca\033[0m! I am forever grateful.")
        print(
            "But we're still living under the fear of \u001b[31;1mChris\033[0m the dragon. Please kill him to save "
            "the Dragon Coast.")


def heca(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Updates the quest status related to finding Heca, based on the character's current quest progress.

    :param character: a dictionary representing a character
    :precondition: character must contain shawn_quest and heca_found
    :postcondition: if shawn_quest is True and heca_found is False, the function updates heca_found to True,
    and print messages to the user
    :postcondition: if heca_found is already True, a brief message is printed
    :postcondition: if shawn_quest is False or not present, a message indicates that the character is unrecognized
    """
    if character["shawn_quest"] and character["heca_found"] is False:
        heca_lines = [
            "\u001b[36mHeca\033[0m: Yes, Shawn is my father! Thank you so much for finding me!",
            "I was lost in the forest. My father must be worried sick.",
            "Let's go back to my father!"
        ]
        for line in heca_lines:
            print(line)
            time.sleep(1)
        character["heca_found"] = True
    elif character["shawn_quest"] and character["heca_found"]:
        print("\u001b[36mHeca\033[0m: Let's go back to my father!")
    else:
        print("\u001b[31;1m???\033[0m: I don't know you. Leave me alone!")


def heca_found(character: dict[str, str | int | bool | dict[str, int]], board: dict) -> dict[tuple[int, int], str]:
    """
    Updates the game board to change heca's location to Desert once she has been found.

    :param character: a dictionary representing a character
    :param board: a dictionary mapping (x, y) coordinated tuples to strings describing the area
    :precondition: character must contain shawn_quest and heca_found keys
    :precondition: board must accurately represent the game's areas and include heca
    :postcondition: if the specified conditions are met, heca's location on the board is updated to Desert
    :return: the updated board dictionary with heca's location changed to Desert if the conditions are met.
    """
    if character["shawn_quest"] is False and character["heca_found"]:
        heca_coord = (key for key, val in board.items() if val == "heca")
        board[heca_coord] = "Desert"
        return board


def david(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Manages a quest given by david, asking for help to collect tree branches.

    :param character: a dictionary representing a character
    :precondition: character must have keys for david_quest, tree_branches, and gold
    :postcondition: if the quest is accepted, david_quest is set to True
    :postcondition: if character has tree branches more than 10, david_quest is set to False,
    tree_branches is decreased by 10, and the character receives a gold reward
    :postcondition: if complete the quest, print a final message from david
    """
    if character["david_quest"] is None:
        say_hi = input(
            "You met \u001b[34;1mDavid\033[0m, the carpenter. Do you want to talk to him? (Y/N): ").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N: ").strip().lower()
        if say_hi == "y":
            print(
                "\u001b[34;1mDavid\033[0m: Hello there! My name is \u001b[34;1mDavid\033[0m. "
                "Please, I need your help..")
            time.sleep(1)
            user_action = input(
                "I haven't had noodles for a couple months now because my last pair of chopsticks broke. Can you help "
                "me collect some tree branches so I can make some more? (Y/N): ").strip().lower()
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N: ").strip().lower()
            responses = {
                "y": "\u001b[34;1mDavid\033[0m: Thank you so much! I need 10 tree branches.\n"
                     "You can find them by defeating some monsters in the forest.",
                "n": "\u001b[34;1mDavid\033[0m: I understand. I mean... I guess I'll continue eating something else.."
            }
            if user_action == "y":
                print(responses["y"])
                character["david_quest"] = True
            else:
                print(responses["n"])
    elif character["david_quest"] and character["tree_branches"] < 10:
        print(
            f"\u001b[34;1mDavid\033[0m: I need 10 tree branches... {character["tree_branches"]} is not enough. Please "
            f"get some more.")
    elif character["david_quest"] and character["tree_branches"] >= 10:
        character["gold"] += 100
        character["david_quest"] = False
        character["tree_branches"] -= 10
        print(
            "\u001b[34;1mDavid\033[0m: Thank you so much! Now I can eat my favorite noodles gracefully. I am forever "
            "grateful.")
        time.sleep(1)
        print("\u001b[34;1mDavid\033[0m: Please take these as a token of my gratitude.")
        time.sleep(1)
        print("You received \u001b[37;1m 100 \u001b[37mGold\033[0m.")
        time.sleep(1)
        print(f"You now have \u001b[37;1m {character["gold"]} \u001b[37mgold\033[0m.")
    else:
        print(
            "\u001b[34;1mDavid\033[0m: Thank you for getting me those tree branches! I don't know what I would have "
            "done without these chopsticks!")
        print(
            "But we're still living under the fear of \u001b[31;1mChris\033[0m the dragon. Please kill him to save "
            "the Dragon Coast.")


def get_valid_elixir_quantity(prompt: str):
    """
    Prompts the user for an integer quantity of elixirs, ensuring the input is valid and greater than 0.

    :param prompt: a string containing the message to display to the user when asking for input
    :precondition: the input for quantity should be an integer
    :postcondition: return an integer representing a valid quantity of elixirs as input by the user
    :return: an integer representing the quantity of elixirs
    """
    while True:
        try:
            quantity = int(input(prompt))
            if quantity < 0:
                print("Quantity must be an integer greater than 0.")
            else:
                return quantity
        except ValueError:
            print("You need to enter a valid integer greater than 0.")


def daniel(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Facilitates an interaction between the character and daniel for purchasing elixirs.

    :param character: a dictionary representing a character
    :precondition: character must contain gold and elixir keys
    :postcondition: if the player decides to buy elixirs and has enough gold, gold is decreased by the
    total purchase cost, and elixir is increased by the quantity bought
    :postcondition: print message if user try to buy more elixirs than their gold allows
    :postcondition: print feedback on the transaction outcome, including any adjustments to the character's gold
    and elixir count
    """
    say_hi = input(
        "You met \u001b[34;1mDaniel\033[0m, the apothecary. Do you want to talk to him? (Y/N): ").strip().lower()
    while say_hi not in ["y", "n"]:
        say_hi = input("Invalid input. Please enter Y or N: ").strip().lower()
    if say_hi == "y":
        welcome_lines = [
            "\u001b[34;1mDaniel\033[0m: Hello there! My name is \u001b[34;1mDaniel\033[0m. I'm the local apothecary.",
            "You can buy more elixirs from me to help you on your journey."
        ]
        for line in welcome_lines:
            print(line)
            time.sleep(1)
        user_action = input("\u001b[34;1mDaniel\033[0m: Would you like to buy some elixirs? (Y/N): ").strip().lower()
        while user_action not in ["y", "n"]:
            user_action = input("Invalid input. Please enter Y or N: ").strip().lower()
        if user_action == "y":
            elixir_price = 50
            maximum_purchase = character["gold"] // elixir_price
            elixir_quantity = get_valid_elixir_quantity(  # Call valid_elixir_quantity function
                f"\u001b[34;1mDaniel\033[0m: How many elixirs would you like to buy?"
                f"They are {elixir_price} gold each: ")
            if elixir_quantity == 0:  # Player buys 0
                print("\u001b[34;1mDaniel\033[0m: So you don't want to buy any elixirs at this time, eh?"
                      "Sure. Come back if you change your mind.")

            while elixir_quantity * elixir_price > character["gold"]:  # See if player has enough gold
                print(f"\u001b[34;1mDaniel\033[0m: You don't have enough gold. "
                      f"You can buy up to {maximum_purchase} elixirs. ")
                elixir_quantity = get_valid_elixir_quantity(f"How many would you like to buy?: ")

            character["gold"] -= elixir_quantity * elixir_price
            character["elixir"] += elixir_quantity
            print(f"You bought {elixir_quantity} elixirs.")
            print(f"You now have {character["elixir"]} elixirs and {character["gold"]} gold.")


def ending(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Unveils the game's ending narrative, reflecting on the character's impact on the world
    and presenting a final choice.

    :param character: a dictionary representing a character
    :precondition: character must contain class and name
    :postcondition: based on the user's choice, character is updated with a new class and their skills are refreshed
    """
    scripts = [
        "Chris (with his last breath): See the world through my eyes, and understand the truth you refused to see.",
        "The player returns to the villages and landscapes they once 'saved', only to find them in ruins or eerily "
        "silent.",
        'NPCs, now fearful, whisper among themselves as the player approaches, branding them not as a hero but as '
        '"The True Devil of Dragon Coast."',
        "Environmental cues highlight the destruction: withered lands, extinguished fires, and monuments once erected "
        "in the player's honor now defaced.",
        "With the fall of Chris, the scales of Dragon Coast tip into darkness. The hero, once revered, now walks a "
        "path lined with the shadows of their deeds.",
        "A new legend begins—not of a savior, but of a harbinger who bore the world's end on their shoulders."
    ]
    for line in scripts:
        print(line)
        time.sleep(3)
    print(f"Heca: Please...{character['name']} stop killing innocents")
    user_input = input("You can accept or deny her final request accept/deny? ")
    user_input = user_input.lower()
    if user_input == "accept":
        print("I see now the destruction I've wrought. I am the architect of Dragon Coast's demise. "
              "It's time I make amends, not as a hero, but as a guardian.")
        character["class"] = "Guardian"
        character_functions.update_skills(character)
    else:
        print("They misunderstand. I did what I had to do. If being the devil means shouldering the world's hate to "
              "bring about change, then so be it.")
        character["class"] = "Devil"
        character_functions.update_skills(character)


def skill_fire_breath(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Simulates a dodging attempt against a dragon's fire breath attack in a combat scenario.

    :param character: a dictionary representing a character
    :precondition: character must contain a hp key
    :postcondition: if the user fails to dodge the dragon's fire breath, hp is decreased by 700
    :postcondition: if the user successfully dodges the attack, the character's hp remains unchanged
    """
    print("Danger looms! Chris inhales deeply, preparing to unleash his dragon breath!!")
    user_choice = input("Quick! Enter 'up', 'down', 'left', or 'right' to dodge the inferno!!")
    user_choice = user_choice.lower()
    dragon_breath = ['up', 'down', 'left', 'right']
    if user_choice == random.choice(dragon_breath) or user_choice not in dragon_breath:
        character["hp"] -= 700
        print("Engulfed by flames, agony consumes you!!!")
        print(f"Reeling from the blow, you're left with {character['hp']} health!!")
    else:
        print("With agility, you evade the deadly flames!")


def skill_question(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Challenges the character with a memory test, impacting their maximum health based on their response.

    :param character: a dictionary representing a character
    :precondition: character must contain a max_hp key
    :postcondition: if the user successfully recalls and inputs the correct word,
    the character's state remains unchanged
    :postcondition: if the user fails to recall the word, the character's max_hp is reduced by 100
    """
    print("Chris eyes you with a cunning glint. 'Let's test your agility,' he smirks.")
    print("'Catch a glimpse of this word; it will vanish in 0.3 seconds. Be ready...'")
    print("Open your eyes...")
    time.sleep(3)
    random_words = ['dog', 'cat', 'rat', 'pet']
    answer = random.choice(random_words)
    print(answer)
    time.sleep(0.3)
    print("\n" * 100)
    user_answer = input("What was the word? Speak quickly: ")
    if user_answer == answer:
        print("'Impressive,' Chris nods, acknowledging your sharpness.")
    else:
        character["max_hp"] -= 100
        print("Chris's curse weaves its dark magic, reducing your vigor. Your maximum health decreases...")
        print(f"Wrong answer. Now, your vitality's ceiling is a mere {character['max_hp']}.")


def battle_chris(character: dict[str, str | int | bool | dict[str, int]], dragon_chris: dict[str, int | str]):
    """
    Engages the player's character in a combat encounter with Dragon Chris, featuring skill selection,
    damage calculation, and dynamic reactions from Chris.

    :param character: a dictionary representing a character
    :param dragon_chris: a dictionary representing dragon chris
    :precondition: character must contain a hp key
    :precondition: dragon_chris must contain health and type keys
    :postcondition: the character's hp may be reduced based on the outcome of dragon chris
    :postcondition: dragon chris's health is reduced based on the damage dealt by character
    :postcondition: if dragon chris's health drops to or below 0, the battle is won, and the function terminates
    :postcondition: if the character's hp drops to or below 0, it results in a game over
    """
    chosen_skill, chosen_type = combat.choose_skill(character)
    damage_dealt = combat.calculate_skill_damage(chosen_skill, chosen_type, character, dragon_chris)
    print(f"Unleashing {chosen_skill}, you inflict {damage_dealt} damage upon Chris.")
    dragon_chris['health'] -= damage_dealt
    if dragon_chris['health'] <= 0:
        print(f"You've defeated Chris!")
        return
    print(f"Chris is still alive with {dragon_chris['health']} health left.")
    dragon_chris['type'] = random.choice(["fire", "water", "grass", "normal"])
    print(f"An enigmatic aura envelops Chris, transforming him into a {dragon_chris['type']} dragon!!!")
    dragon_skills = ['attack', 'fire breath', 'question']
    skill = random.choice(dragon_skills)
    if skill == "attack":
        print("Chris unleashes a devastating attack, dealing 500 damage to you!!")
        character["hp"] -= 500
        print(f"Reeling from the blow, you're left with {character['hp']} health!!")
    elif skill == "fire breath":
        skill_fire_breath(character)
    elif skill == "question":
        skill_question(character)
    if character['hp'] <= 0:
        print("Game Over")
        return


def chris(character: dict[str, str | int | bool | dict[str, int]]):
    """
    Initiates the final encounter with Chris, the dragon, blending narrative elements with combat mechanics.

    :param character: a dictionary representing a character
    :precondition: character must contain name and location
    :postcondition: if user won, character's location is updated to home
    """
    dragon_chris = {'health': 5000, 'type': random.choice(["fire", "water", "grass", "normal"])}
    print("You've encountered the dragon Chris!!")
    print(f"Chris has {dragon_chris['health']} hp and type is {dragon_chris['type']}")
    print("Chris: You've come far, hero. But have you ever questioned why I'm the enemy? "
          "Who decided I was the villain?")
    time.sleep(2)
    print(f"{character['name']}: You threaten all of Dragon Coast! Your reign ends now.")
    print("Chris: Look around. Who brought more harm? "
          "I, who sought to protect my realm,"
          "or you, who blindly followed a path of destruction?")
    while dragon_chris['health'] > 0:
        # Let the user choose a skill
        battle_chris(character, dragon_chris)
    character["chris"] = True
    ending(character)
    character["location"] = {"x-coordinate": 6, "y-coordinate": 2}
