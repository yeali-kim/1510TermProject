import time
import character_functions


def jinkx(character):
    if character['class'] == 'Citizen': #check if class is Citizen
        say_hi = input("You met \033[1;35mJinkx\033[0m. Do you want to talk to her? (Y/N)").strip().lower() # ask user if they want to talk to Jinkx
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\033[1;35mJinkx\033[0m : Hi there little fella! My name is \033[1;35mJinkx\033[0m, the wise wizard!")
            time.sleep(1)
            print("I can teach you some magic spells.")
            time.sleep(1)
            user_action = input("Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn magic spells
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mJinkx\033[0m : Wonderful! Let's start right away. Abracadabra!",
                "n": "\033[1;35mJinkx\033[0m : Fine. You don't look like a wizard material anyways."
                }
            if user_action == "y":
                character['class'] = 'Magician' #set class to Magician
                character_functions.update_skills(character) #update skills
                lines = [
                    responses["y"],
                    "...",
                    "...",
                    "Great job surviving through the training.",
                    "You are now a \033[92mmagician\033[0m!",
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
        print("\033[1;35mJinkx\033[0m : You are already a knight. Chrissipus will be disappointed.")
    else:
        print("\033[1;35mJinkx\033[0m : You are already an archer. Hypatia will be disappointed.")
    return character


def chrissipus(character):
    if character['class'] == 'Citizen': #check if class is Citizen
        say_hi = input("You met \033[1;35mChrissipus\033[0m. Do you want to talk to him? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\033[1;35mChrissipus\033[0m : Hi there young man! My name is \033[1;35mChrissipus\033[0m, the mighty knight!")
            time.sleep(1)
            print("I can teach you some sword skills.")
            time.sleep(1)
            user_action = input("Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn sword skills
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mChrissipus\033[0m : I knew it! Grab your sword my friend! Not that one. That one is expensive.",
                "n": "\033[1;35mChrissipus\033[0m : Fine. Pfft, look at your size anyways."
                }
            if user_action == "y":
                character['class'] = 'Knight' #set class to Knight
                character_functions.update_skills(character) #update skills
                lines = [
                    responses["y"],
                    "...",
                    "...",
                    "Great job surviving through the training.",
                    "You are now a \033[92mknight\033[0m!",
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
        print("\033[1;35mChrissipus\033[0m : You are already a magician. Jinkx will be disappointed.")
    else:
        print("\033[1;35mChrissipus\033[0m : You are already an archer. Hypatia will be disappointed.")
    return character


def hypatia(character):
    if character['class'] == 'Citizen': #check if class is Citizen
        say_hi = input("You met \033[1;35mHypatia\033[0m. Do you want to talk to her? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\033[1;35mHypatia\033[0m : Hi there young man! My name is \033[1;35mHypatia\033[0m, the great archer!")
            time.sleep(1)
            print("I can teach you some archery skills.")
            time.sleep(1)
            user_action = input("Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn archery skills
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mHypatia\033[0m : Hypatia: I knew it! I will make you the best archer in the world!",
                "n": "\033[1;35mHypatia\033[0m : Fine. You look clumsy anyways. Archery is not for everyone."
                }
            if user_action == "y":
                character['class'] = 'Archer' #set class to Archer
                character_functions.update_skills(character) #update skills
                lines = [
                    responses["y"],
                    "...",
                    "...",
                    "Great job surviving through the training.",
                    "You are now an \033[92marcher\033[0m!",
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
    return character


def shawn(character):
    say_hi = input("You met Shawn. Do you want to talk to him? (Y/N)")
    if say_hi == "y":
        responses = {
            "y": "Shawn: Thank you so much! Please find my daughter. She was last seen in the forest.",
            "n": "Shawn: I understand. It's a difficult task. I'll just keep waiting."
        }
        user_action = input("Shawn: My daughter Heca has been missing for a month. Can you help me find her? (Y/N)")
        if user_action in ["y", "n"]:
            if user_action == "y":
                print(responses["y"])
                shawn_quest(character)
            else:
                print(responses["n"])
        else:
            response = "Invalid input. Please enter Y or N"


def shawn_quest(character):
    responses = {
        "greeting": "My daughter Heca has been missing for a month. Can you help me find her? (Y/N)",
        "yes_response": "Thank you so much! Please find my daughter. She was last seen in the forest.",
        "no_response": "I understand. It's a difficult task. I'll just keep waiting.",
        "fulfilled": "Thank you so much for finding my daughter! Here is a reward for you.",
        "unfulfilled": "I'm still waiting for you to find my daughter. Please hurry."
    }
    print(responses["greeting"])


def david(character):
    responses = {
        "greeting": "I need some tree branches to make chopsticks with. Can you help me? (Y/N)",
        "yes_response": "Great! I need 10 branches. Bring them to me and I'll reward you.",
        "no_response": "I understand. Let me know if you change your mind.",
        "fulfilled": "Thank you so much! Here is your reward.",
        "unfulfilled": "I'm still waiting for those branches. Please hurry."
    }
    print(responses["greeting"])


def daniel(character):
    responses = {
        "greeting": "Welcome to my shop! Full health elixirs are 100G each. Would you like to buy one? (Y/N)",
        "yes_response": "Great! That will be 100G.",
        "no_response": "No worries. My potions are always available.",
        "fulfilled": "Thank you for your purchase! Use your elixir wisely.",
        "unfulfilled": "You don't have enough gold to buy a potion. Come back when you do."
    }
    print(responses["greeting"])


def daughter(character):
    responses = {
        "greeting": "Thank you for finding me! I was lost in the forest. My father must be worried sick."
    }
    print(responses["greeting"])


def chris(character):
    responses = {
        "greeting": "How dare you enter my lair! Prepare to face my wrath!"
    }
