# 1510TermProject
## Contributors:

--------------------------
### Name: Seogin Hong
### Student Number: A01353628
### GitHub Name: seogin

--------------------------
### Name: Yeali Kim
### Student Number : A00985734
### GitHub Name: yeali-kim

## Any important comments you'd like to make about your work:
We are very excited to share our very first Python text based game project!

## Text-Based Adventure Game
This is a SUD (Single User Dungeon) game. 
In this game, you play as a hero who has set off to save Dragon Coast from dragon Chris. 
- Player starts from Home, located at (6, 2).
- Returning home will fully heal the player.
- The game encourages the player to go to the school to get a class first.
- There are 12 unique creatures to encounter, and 4 types, "Fire", "Water", "Grass", and "Normal".
  Choose your skills carefully based on your enemy's type!
  Using wrong types will increase your enemy's health instead of decreasing it.
Have Fun, Hero!

## How to Play
1. Run the main() function from the main_game file.
2. Players input directions (w, a, s, d) to navigate through the map.

## Creatures
>Forest

|        | Rabbit | Gump   | Stump | Wild Boar |
|--------|--------|--------|-------|-----------|
| HP     | 10     | 20     | 30    | 50        |
| Damage | 5      | 10     | 15    | 20        |
| EXP    | 80     | 100    | 120   | 130       |
| Type   | Grass  | Normal | Grass | Grass     |

>Desert

|        | Scorpion | Skeleton | Golem | Sand Serpent |
|--------|----------|----------|-------|--------------|
| HP     | 100      | 200      | 300   | 500          |
| Damage | 30       | 50       | 70    | 100          |
| EXP    | 150      | 200      | 300   | 350          |
| Type   | Fire     | Normal   | Water | Normal       |

>Castle

|        | Cerberus | Gargoyle | Lich  | Death Knight |
|--------|----------|----------|-------|--------------|
| HP     | 700      | 1000     | 1000  | 2000         |
| Damage | 200      | 300      | 700   | 500          |
| EXP    | 500      | 800      | 1000  | 1500         |
| Type   | Fire     | Normal   | Water | Normal       |


## Type Chart
|        | Fire | Water | Grass | Normal | 
|--------|------|-------|-------|--------|
| Fire   | 50%  | -50%  | 200%  | 100%   |
| Water  | 200% | 50%   | -50%  | 100%   |
| Grass  | -50% | 200%  | 50%   | 100%   |
| Normal | 100% | 100%  | 100%  | 100%   |

## Mandatory Python Elements

| Description         | Line of Code                       |
|---------------------|------------------------------------|
| Function Recursion  | Line 162 in character_functions.py |
| Itertools           | Line 58 in combat.py               |
| Function Annotation | Line 210 in character_functions.py |
| Using exception     | Line 172 in combat.py              |
| Random module       | Line 323 in combat.py              |
| Membership Operator | Line 142 in combat.py              |
| Range Function      | Line 35 in board.py                |
| Enumerate Function  | Line 149 in character_functions.py |
| While loop          | Line 179 in character_functions.py |
| If Statement        | Line 388 in npc.py                 |
| Mutable Data        | Line 29 in character_functions.py  |
| Immutable Data      | Line 65 in board.py                |

## Technologies and Resources Used
- Python 3.12.1
- Python.org
- COMP 1510 Notes
