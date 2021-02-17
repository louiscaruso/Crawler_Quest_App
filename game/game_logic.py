from art import *
import re
from colorama import Fore, Back, Style
from kary import KaryTree, KaryNode


def game_logic():
    title = text2art("Crawler Quest", chr_ignore=True)
    print(Fore.RED + title)
    print(Style.RESET_ALL) 
    print(Fore.BLUE)
    print("""
    *****************
    Welcome
    to
    the 
    thunderdome
    *****************
    """)
    start_game = input("""
    (s)tart Game
    (q)uit Game
    """)
    print(Style.RESET_ALL) 
    if start_game == "s":
        play()
    else:
        quits()

def play():
    file = read_file('./assets/story.txt')
    story = process_story(file)
    print(story['{start}'])
    choice =input(f"""
    What will you do?
    (q)Dungeon
    (w)Town
    (e)Path
    """)
    if choice == 'q':
        print(story['{dungeon}'])
    elif choice == 'w':
        print(story['{town}'])
    elif choice == 'e':
        print(story['{path}'])



def read_file(txt_file):
    with open(txt_file) as text:
        story_base = text.read()
        return story_base

def store_story(story_txt):
    parsed = tuple(re.findall("\[[^\]]*\]", story_txt , re.IGNORECASE))
    return parsed
    
def process_story(txt_file):
    story_keys = {}
    count = 0
    key_Nodes = tuple(re.findall("\{.*?\}", txt_file, re.IGNORECASE))
    for key in key_Nodes:
        # print(key)
        story_keys[f'{key}'] = []
    
    para = store_story(txt_file)
    # print(para)
    for key in story_keys.keys():
        story_keys[f'{key}'].append(para[count])
        count += 1
    
    print(story_keys.keys())
    return story_keys


    

def fight(Character, Monster):
    turn = 0
    rounds = 0
    while Character.vitality and Monster.vitality:
        if not turn:
            take_turn(Character)
            turn += 1
        else:
            take_turn(Monster)
            turn -= 1
            rounds += 1

def take_turn(actor):
    if actor.id == "c":
        take_t = input("""
        (A)ttack
        (D)efend
        """)

        if take_t == "A":
            damage = Character.strength - Monster.defense
            if damage == 0:
                damage = 1
            Monster.vitality -= damage
        elif take_t == "D":
            Character.defend()
    elif actor.id == "m":
        actor.behavior()
        



def gameover(cause):
    endgame = text2art(f"{cause}", chr_ignore=True)
    print(endgame)
    endgame_input = input("""
    (Q)uit
    (R)estart
    """)
    if endgame_input == "Q":
        quits()
    else:
        play()

def quits():
    pass

if __name__ == "__main__":
    game_logic()
    # story_txt = read_file('./assets/story.txt')
    # print(store_story(story_txt))
    # process_story(story_txt)






    # count = 0
    # children = []
    # root = KaryNode(key_Nodes[0])
    # story_tree = KaryTree(root)
    # # print(story_tree.root.value)
    # scene_parse = tuple(re.findall("\[.*?\]",txt_file, re.IGNORECASE))
    # for scene in range(len(scene_parse)):
    #     children_parse = tuple(re.findall("\(.*?\)",scene_parse[scene], re.IGNORECASE))
    #     if count == 0:
    #         root.children.append(KaryNode(children_parse[0]))
    #         root.children.append(KaryNode(children_parse[1]))
    #         root.children.append(KaryNode(children_parse[2]))
    #         count += 1
    #     children.append(children_parse)
    # saplings = root.children
    # for child in range(len(saplings)):
        
    #     children_parse = tuple(re.findall("\(.*?\)",scene_parse[scene], re.IGNORECASE))
    #     for grand_child in range(len(children_parse)):
    #         saplings[child].children.append(KaryNode(children_parse[grand_child]))


    # return story_tree
    # #    
    # #     else:
    # #         child = root.children[]
    # #         child.children.append(KaryNode(children_parse[scene]))
    # #         count +=1
    
    # # return story_tree