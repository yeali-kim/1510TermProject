import time
import character_functions


def jinkx(character):
    say_hi = input("You met \033[1;35m Jinkx \033[0m. Do you want to talk to her? (Y/N)").strip().lower()
    while say_hi not in ["y", "n"]:
        print("Invalid input. Please enter Y or N")
        say_hi = input("You met \033[1;35m Jinkx \033[0m. Do you want to talk to her? (Y/N)").strip().lower()
    if say_hi == "y":
        user_action = input("\033[1;35m Jinkx \033[0m : Hi there little fella! My name is \033[1;35m Jinkx \033[0m , the wise wizard!\nI can teach you some magic spells. Would you like to learn some? (Y/N)")
        while user_action not in ["y", "n"]:
            print("Invalid input. Please enter Y or N")
            user_action = input("\033[1;35m Jinkx \033[0m : Hi there little fella! My name is \033[1;35m Jinkx \033[0m , the wise wizard!\nI can teach you some magic spells. Would you like to learn some? (Y/N)")
        responses = {
            "y": "\033[1;35m Jinkx \033[0m : Wonderful! Let's start right away. Abracadabra!",
            "n": "\033[1;35m Jinkx \033[0m : Fine. You don't look like a wizard material anyways."
            }
        if user_action == "y":
            character['class'] = 'Magician' #set class to Magician
            character_functions.update_skills(character) #update skills
            lines = [
                responses["y"],
                "...",
                "...",
                "Great job surviving through the training.",
                "You are now a wizard!",
                "Use your new skills wisely.",
                '\033[92m' + f"Your class is now {character['class']}.",
                '\033[92m' + f"Now you can use these skills. {character['skills']}." + '\033[0m'
            ]
            for line in lines:
                print(line)
                time.sleep(0.2)
        else:
            print(responses["n"])
        
    return character


def chrissipus(character):
    say_hi = input("You met Chrissipus. Do you want to talk to him? (Y/N)")
    if say_hi == "y":
        responses = {
            "y": "Chrissipus: I knew it! Grab your sword my friend! Not that one. That one is expensive.",
            "n": "Chrissipus: Fine. Pfft, look at your size anyways."
        }
        user_action = input(
            "Chrissipus: Hi there young man! My name is Chrissipus, the mighty knight!\nI can teach you some sword skills. Would you like to learn some? (Y/N)")
        if user_action in ["y", "n"]:
            if user_action == "y":
                print(responses["y"])
                print(
                    "...\n...\nGreat job surviving through the training.\nNow you are a knight!\nUse your new skills wisely.")
                character['class'] = 'Knight'
                print('\033[92m' + f"Your class is now {character['class']}." + '\033[0m')
                return character
            else:
                print(responses["n"])
        else:
            response = "Invalid input. Please enter Y or N"


def hypatia(character):
    say_hi = input("You met Hypatia. Do you want to talk to her? (Y/N)")
    if say_hi == "y":
        responses = {
            "y": "Hypatia: I knew it! I will make you the best archer in the world!",
            "n": "Hypatia: Fine. You look clumsy anyways. Archery is not for everyone."
        }
        user_action = input(
            "Hypatia: Hi there little one! My name is Hypatia, the great archer!\nI can teach you some archery skills. Would you like to learn some? (Y/N)")
        if user_action in ["y", "n"]:
            if user_action == "y":
                print(responses["y"])
                print(
                    "...\n...\nGreat job surviving through the training.\nNow you are a archer!\nUse your new skills wisely.")
                character['class'] = 'Archer'
                print('\033[92m' + f"Your class is now {character['class']}." + '\033[0m')
                return character
            else:
                print(responses["n"])
        else:
            response = "Invalid input. Please enter Y or N"


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
