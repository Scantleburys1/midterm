import sys
import random
coins=0
strength= random.randint(10,100)
choice= input()
def coin_update(sum):
    global coins
    coins+=sum 
def adventure_start():
    print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears.\n You have no memory of how you got here. As you get up and dust yourself off, you notice two paths ahead.")
    print("On your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water")
    print("On your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers echoing from within.")
    print("\nWhat will you decide?\nLeft\nRight")
if choice==('left'or'Left'):
    print(coins)
def left():
    print("The tunnel leads to a stream. Follow it downstream or upstream?")
    choice
def right():
    print("You walk down the path to a small clearing.")
    print("Would you like to 'look' around, 'follow' the whispers, or go 'right'") 
    choice
if choice==():
    print(coins)
def l_upstream():
    print("You follow the stream upstream. You see something shiny flickering in the shallow water as you walk.\nWould you like to check it out?")
    print("Yes or No?")
    choice
    if choice==('yes'or'Yes'):
        coin_update(100)
    elif choice==('no'or'No'):
        print("You have decided to keep going.")
    print("You continue upstream. It leads to a mildly steep cliffside where a dim light shines at the top.\nWill you 'Climb'up or 'Go Back'?")
    choice
def l_climb():
    print("You get to the top successfully. You spot a slim opening where the light originates from. You squeeze through. Now outside, you see three young women standing on the side of the stream.")
    print("They notice you and begin to approach you. What will you do?\n 'Run'!\n 'Show' your coins")
    choice
    if choice==('Show'or'show')and coins>=99:
        print("You are lead to a hidden village and brought in front of the Village Chief. Showing your riches, you are deemed a gift from the gods and are celebrated as such.")
        print("Ending 1")
    elif choice==('Run'or'run'):
        print("run")
def l_run():
    print("You run! Soon you run straight into a village clearing. You are taken away by guards nearby and are presented in front of the Village Chief!")
    print("They speak in a foreign language around you. You are then nudged by spears closer to the Chief. What will you do?\n Say 'Nothing'\n 'Show' your coins")
    choice
    if choice==('Show'or'show')and coins>=99:
        print("You are spared. Without much to lose, you stick around and integrate yourself into their society.")
        print("Ending 2")
        sys.exit()
    elif choice==('Nothing'or'nothing'):
        print("You've sealed your fate. You become sacrifice to their God of Protection. Cool Guy.")
        print("Ending 3")
        sys.exit()
def l_downstream():
    print("Following the stram downstream, you reach a waterfall. How will you get down?\n 'Jump'?\n 'Look' Around?")
    choice
    if choice==('Jump'or'jump'):
        print("Wow! Such a brave soul!\n You jump, but unforunately hit your head on a rock upon impact.\n You died and your spirit becomes bound to the small lake below.")
        print("Ending 4")
        sys.exit()
    elif choice==('Look'or'look'):
        print("You see a pattern of rocks along the wall to the left of the waterfall. It looks like a set of stairs. You try your luck and travel down.")
        print("After safely getting down, you see a dim light coming from a small tunnel across the lake, but something calls you towards a dark path to your left.")
        print("What will you decide?\n'Tunnel'\n 'Dark path'")
        choice
if choice==('tunnel'):
    print(l_escape)
def l_dark():
    print("The dark path leads you to a cave room filled with gold! You're rich!")
    print("Suddenly, you hear a hiss from one of the dark corners of the room. A poisonous snake! What will you do?\n 'Run'!\n 'Fight' with your bare hands!")
    choice
    if choice==('Run'or'run'):
        print("You run away! Not without taking some change.")
        print(l_escape)
        coin_update(20)
        sys.exit()
    elif choice==('Nothing'or'nothing'):
        print("")
        print("Ending 3")
        sys.exit()
def l_escape():
    print("You escaped!")
    if coins<=30:
        print("You now travel aimlessly, trying to make a living. You dont have enough to integrate into nearby societies...")
        print("Ending 5")
    else:
        print("You live a humble life in a nearby kingdom. Yet, every day until death, you think about what could've been.")
        print("ending 6")
def l_fight():
    print("You put your fists up and duke it out with the snake!")
    if strength>=60:
        print("You take a rock and smash it over the snakes head crushing it! You've won and now have all the gold in the world to celebrate!")
        print("Ending 7")
        sys.exit()
    elif strength>=20:
        print("The snake bites you, hard! You stagger then fall to the floor, venom coursing through your veins. It's over.")
        print("Ending 8")
        sys.exit()

