import random

def make_npc(board):
    npc_coords = {
        'school':
            {(0, 0): {'name': 'Jinkx', 'role': 'great magician'},
            (0, 3): {'name': 'Chrissipus', 'role': 'great knight'},
            (2, 2): {'name': 'Archie', 'role': 'great archer'}},
        'town': 
            {(4, 1): {'name': 'David', 'role': 'carpenter'},
            (6, 0): {'name': 'Daniel', 'role': 'apothecary'}, 
            (5, 4): {'name': 'Shawn', 'role': 'mayor'}},
        'castle':
            {(10, 10): {'name': 'Draco', 'role': 'dragon'}},
        'forest':
            {(random.randint(8, 11), random.randint(0, 8)): {'name': 'Heca', 'role': 'daughter'}}
    }

    # Place NPCs on the board
    for place, coords in npc_coords.items():
        for coord, npc_info in coords.items():
            board[coord] = f"NPC({npc_info['name']}, {npc_info['role']})"



def npc_response():
    school_npc_greet = [
        ("great wizard", "I can teach you some magic spells. Would you like to learn some? (Y/N)"),
        ("great knight", "I can teach you some sword fighting skills. Would you like to learn some? (Y/N)"),
        ("great archer", "I can teach you some archery skills. Would you like to learn some? (Y/N)")
    ]
    
    school_npc_yes_actions = [
        ("great wizard", "I knew it! Let's begin. Avada Kedavra!"),
        ("great knight", "I knew it! Grab your sword my friend! Not that one. That one is expensive."),
        ("great archer", "I knew it! I will make you the best archer in the world.")
    ]
    school_npc_no_actions = [
        ("great wizard", "Fine. I didn't see a great wizard in you anyways."),
        ("great knight", "Fine. You don't look that strong anyways."),
        ("great archer", "Fine. You look clumsy anyways. Archery is not for everyone.")
    ]

    town_npc_greet = [
        ("carpenter", "I need some tree branches to make chopsticks with. Can you help me? (Y/N)"),
        ("apothecary", "Welcome to my shop! I have potions for sale. Would you like to buy some? (Y/N)"),
        ("mayor", "My daughter's been missing for a month. Can you help me find her? (Y/N)")
    ]
    
    town_npc_yes_actions = [
        ("carpenter", "Great! I need 10 branches. Bring them to me and I'll reward you."),
        ("apothecary", "Great! Here are my potions. Choose wisely."),
        ("mayor", "Thank you so much! Please find my daughter. She was last seen in the forest.")
    ]
    
    town_npc_no_actions = [
        ("carpenter", "I understand. Let me know if you change your mind."),
        ("apothecary", "No worries. My potions are always available."),
        ("mayor", "I understand. It's a difficult task. I'll just keep waiting.")
    ]
    
    
    
