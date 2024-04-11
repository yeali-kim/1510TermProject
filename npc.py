import time
import character_functions
import random
import combat


def jinkx(character: dict[str, str | int | bool | dict[str, int]]):
    if character['class'] == 'Citizen':  # check if class is Citizen
        # ask user if they want to talk to Jinkx
        say_hi = input(
            "You met \033[1;35mJinkx\033[0m, the wise wizard. Do you want to talk to her? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\033[1;35mJinkx\033[0m: Hi there little fella! My name is \033[1;35mJinkx\033[0m, the wise wizard!")
            time.sleep(1)
            print("I can teach you some magic spells.")
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
    if character['class'] == 'Citizen':  # check if class is Citizen
        say_hi = input(
            "You met \033[1;35mChrissipus\033[0m, the mighty knight. Do you want to talk to him? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print(
                "\033[1;35mChrissipus\033[0m : Hi there young man! My name is \033[1;35mChrissipus\033[0m, the mighty "
                "knight!")
            time.sleep(1)
            print("I can teach you some sword skills.")
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
    if character['class'] == 'Citizen':  # check if class is Citizen
        say_hi = input(
            "You met \033[1;35mHypatia\033[0m, the great archer. Do you want to talk to her? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print(
                "\033[1;35mHypatia\033[0m: Hi there young man! My name is \033[1;35mHypatia\033[0m, the great archer!")
            time.sleep(1)
            print("I can teach you some archery skills.")
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
    if character["shawn_quest"] is False and character["heca_found"]:
        heca_coord = (key for key, val in board.items() if val == "heca")
        board[heca_coord] = "Desert"
        return board


def david(character: dict[str, str | int | bool | dict[str, int]]):
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
                "y": "\u001b[34;1mDavid\033[0m: Thank you so much! I need 10 tree branches. You can find them by "
                     "defeating some monsters in the forest.",
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
