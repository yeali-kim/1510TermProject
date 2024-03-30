import time
import character_functions
import board


def jinkx(character):
    if character['class'] == 'Citizen': #check if class is Citizen
        say_hi = input("You met \033[1;35mJinkx\033[0m. Do you want to talk to her? (Y/N)").strip().lower() # ask user if they want to talk to Jinkx
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\033[1;35mJinkx\033[0m: Hi there little fella! My name is \033[1;35mJinkx\033[0m, the wise wizard!")
            time.sleep(1)
            print("I can teach you some magic spells.")
            time.sleep(1)
            user_action = input("Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn magic spells
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mJinkx\033[0m: Wonderful! Let's start right away. Abracadabra!",
                "n": "\033[1;35mJinkx\033[0m: Fine. You don't look like a wizard material anyways."
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
        print("\033[1;35mJinkx\033[0m: You are already a knight. Chrissipus will be disappointed.")
    else:
        print("\033[1;35mJinkx\033[0m: You are already an archer. Hypatia will be disappointed.")
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
                "y": "\033[1;35mChrissipus\033[0m: I knew it! Grab your sword my friend! Not that one. That one is expensive.",
                "n": "\033[1;35mChrissipus\033[0m: Fine. Pfft, look at your size anyways."
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
        print("\033[1;35mChrissipus\033[0m: You are already a magician. Jinkx will be disappointed.")
    else:
        print("\033[1;35mChrissipus\033[0m: You are already an archer. Hypatia will be disappointed.")
    return character


def hypatia(character):
    if character['class'] == 'Citizen': #check if class is Citizen
        say_hi = input("You met \033[1;35mHypatia\033[0m. Do you want to talk to her? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\033[1;35mHypatia\033[0m: Hi there young man! My name is \033[1;35mHypatia\033[0m, the great archer!")
            time.sleep(1)
            print("I can teach you some archery skills.")
            time.sleep(1)
            user_action = input("Would you like to learn some? (Y/N)").strip().lower()  # ask user if they want to learn archery skills
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\033[1;35mHypatia\033[0m: Hypatia: I knew it! I will make you the best archer in the world!",
                "n": "\033[1;35mHypatia\033[0m: Fine. You look clumsy anyways. Archery is not for everyone."
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
    if character["shawn_quest"] == None:
        say_hi = input("You met \u001b[34;1mShawn\033[0m. Do you want to talk to him? (Y/N)").strip().lower()
        while say_hi not in ["y", "n"]:
            say_hi = input("Invalid input. Please enter Y or N").strip().lower()
        if say_hi == "y":
            print("\u001b[34;1mShawn\033[0m: Hello there! My name is \u001b[34;1mShawn\033[0m. I need your help.")
            time.sleep(1)
            print("My daughter \u001b[31;1mHeca\033[0m has been missing for a month. Can you help me find her? (Y/N)")
            while user_action not in ["y", "n"]:
                user_action = input("Invalid input. Please enter Y or N").strip().lower()
            responses = {
                "y": "\u001b[34;1mShawn\033[0m: Thank you so much! Please find my daughter. She was last seen in the forest.",
                "n": "\u001b[34;1mShawn\033[0m: I understand. It's a difficult task. I'll just keep waiting."
            }
            if user_action == "y":
                print(responses["y"])
                character["shawn_quest"] = True
            else:
                print(responses["n"])
    elif character["shawn_quest"] == True and character["heca_found"] == False:
        print("\u001b[34;1mShawn\033[0m: I'm still waiting for you to find my daughter \u001b[31;1mHeca\033[0m. Please hurry.")
    elif character["shawn_quest"] == True and character["heca_found"] == True:
        print("\u001b[34;1mShawn\033[0m: Thank you for finding my daughter \u001b[31;1mHeca\033[0m! I am forever grateful.")
        time.sleep(1)
        print("\u001b[34;1mShawn\033[0m: Here is a reward for you.")
        time.sleep(1)
        print("You received \u001b[37;1m3 \u001b[37melixirs\033[0m.")
        character["shawn_quest"] = False
        character["elixir"] += 3
    else:
        print("\u001b[34;1mShawn\033[0m: Thank you for finding my daughter \u001b[31;1mHeca\033[0m! I am forever grateful.")
        

def heca(character):
    if character["shawn_quest"] == True:
        print("\u001b[31;1mHeca\033[0m: Yes, Shawn is my father! Thank you for finding me!") 
        time.sleep(1)
        print("I was lost in the forest. My father must be worried sick.")
        time.sleep(1)
        print("Let's go back to my father!")
        character["heca_found"] = True
    else:
        print("\u001b[31;1m???\033[0m: I don't know you. Leave me alone!")


def heca_found(character, board):
    if character["shawn_quest"] == False and character["heca_found"] == True:
        heca_coord = (key for key, val in board.items() if val == "heca")
        board[heca_coord] = "Forest"
        return board
    

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
        "no_response": "No worries. My elixirs are always available.",
        "fulfilled": "Thank you for your purchase! Use your elixir wisely.",
        "unfulfilled": "You don't have enough gold to buy a elixir. Come back when you do."
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
