#Solina Scantlebury
#Project: Will You Make it Out OK?
#As the title suggest, they are few obstacles in your way, but it's all based on the user's choices that'll determine how dire the consequences may be.
#This game is simply about a character who has no recollection of themselves or how they got there, only trying to find a way out and hopefully integrate back into society.


import sys
import random

coins = 0  # Starting coins
strength = random.randint(10, 100) #Strength sysytem that determines whether some choices fail or succeed
inventory = [] #Applies only to right path

def coin_update(amount):#Update coin count when user finds coins, and only if they find coins.
    global coins
    coins += amount 

def adventure_start():
    global choice
    print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears.")
    print("You notice two paths ahead.")
    print("On your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.")
    print("On your right, a wider passage seems to have some light coming from it. You hear distant whispers echoing from within.")
    choice = input("What will you decide?\n'Left'\n'Right'\n")

    if choice =='left':
        left()
    elif choice == 'right':
        right()
    else:
        print("Invalid Answer. Try Again..")
        adventure_start()

def left(): 
    global choice
    print("The tunnel leads to a stream. Follow it 'downstream' or 'upstream'?")
    choice = input()

    if choice == 'downstream':
        l_downstream()
    elif choice == 'upstream':
        l_upstream()
    else:
        print("Invalid Answer. Try Again..")
        left()

def right(): 
    global choice
    print("You walk down the path to a small clearing.\nYou see the light coming from a hole at the top of the cave.")
    print("To the 'right', you see a small opening. Just enough for you to crawl through..")
    print("Would you like to 'look' around, 'follow' the whispers, or go 'right'?")
    choice = input()

    if choice == 'look':
        r_look()
    elif choice == 'follow':
        r_follow()
    elif choice == 'right':
        r_right()
    else:
        print("Invalid Answer. Try Again..")
        right()

def l_downstream():
    global choice
    print("Following the stream downstream, you reach a waterfall. How will you get down?\n 'Jump'?\n 'Look' Around?")
    choice = input()

    if choice == 'jump':
        print("Wow! Such a brave soul!\nYou jump, but unfortunately hit your head on a rock upon impact.\nYou died.")
        print("Congratulations! You completed Ending 4!\nEnding 4:Your spirit now protects the lake and the riches that lay beyond the waterfall...")#I wanted to hit that this cave is home to the fountain of youth. This version of it keeps the soul alive.
        sys.exit()
    elif choice == 'look':
        print("You see a pattern of rocks along the wall to the left of the waterfall. It looks like a set of stairs. You try your luck and travel down.")
        print("After safely getting down, you see a dim light coming from a small tunnel across the lake, but something calls you towards a dark path to your left.")
        print("What will you decide?\n'Tunnel'\n'Dark path'")
        choice = input()
        if choice == 'tunnel': 
            l_escape()
        elif choice == 'dark path':
            l_darkpath()
        else:
            print("Invalid Answer. Try Again..")
            l_downstream()
    else:
        print("Invalid Answer. Try Again..")
        l_downstream()

def l_upstream():
    global choice
    print("You follow the stream upstream. You see something shiny flickering in the shallow water as you walk.\nWould you like to check it out?")
    choice = input("Yes or No?\n")
    if choice == 'yes':
        coin_update(100)
        print("You found 100 coins!")
    elif choice == 'no':
        print("You have decided to keep going.")
    else:
        print("Invalid Choice. Try again..")
        l_upstream()

    print("You continue upstream. It leads to a mildly steep cliffside where a dim light shines at the top.\nWill you 'Climb' up or 'Go Back'?")
    choice = input()
    if choice == 'climb':
        l_climb()
    elif choice == 'go back':
        l_downstream()
    else:
        print("Invalid Answer. Try Again..")
        l_upstream()

def l_climb():
    global choice
    print("You get to the top successfully. You spot a slim opening where the light originates from.")
    print("Now outside, you see three young women standing on the side of the stream.")
    print("They notice you and begin to approach you. What will you do?\n'Run'!\n'Show' your coins")
    choice = input()
    if choice == 'run':
        l_run()
    elif choice == 'show' and coins >= 99:
        print("You are led to a hidden village and brought in front of the Village Chief. Showing your riches, you are deemed a gift from the gods and are celebrated as such.")
        print("Congratulations! You completed Ending 1!\nEnding 1: You live a lavish life amongst the villagers.") #This game is set in a fantasy world so I wanted to implement other ways of life.
        print(f'Coins: {coins}')
        sys.exit() #ends game, this code was completely new to me
    else:
        print("Invalid Choice. Try Again..")
        l_climb()

def l_run():
    print("You run! Soon you run straight into a village clearing. You are taken away by guards nearby and are presented in front of the Village Chief!")
    print("They speak in a foreign language around you. You are then nudged by spears closer to the Chief. What will you do?\nSay 'Nothing'\n'Show' your coins")
    choice = input()
    if choice == 'show' and coins >= 99:
        print("You are spared. Without much to lose, you stick around and integrate yourself into their society.")
        print("Congratulations! You completed Ending 2!")
        print(f'Coins: {coins}')
        sys.exit()
    elif choice == 'nothing':
        print("You've sealed your fate. You become a sacrifice to their God of Protection.")
        print("Congratulations! You completed Ending 3!")
        print(f'Coins: {coins}')
        sys.exit()
    else:
        print("Invalid Answer. Try Again..")
        l_run()

def l_escape():
    print("You escaped!")
    if coins <= 30:
        print("Congratulations! You completed Ending 5!")
        print("Ending 5: You now travel aimlessly, trying to make a living. You don't have enough to integrate into nearby societies...") #In this world you need more than a mere 30 coins
    else:
        print("Congratulations! You completed Ending 6!")
        print("Ending 6: You live a humble life in a nearby kingdom. Yet, every day until death, you think about what could've been.")
    print(f'Coins: {coins}')
    sys.exit()

def l_darkpath():
    global choice
    print("The dark path leads you to a cave room filled with gold! You're rich!")
    print("Suddenly, you hear a hiss from one of the dark corners of the room. A poisonous snake! What will you do?\n'Run'!\n'Fight' with your bare hands!") #Wanted to add a little danger on this path
    choice = input()
    if choice == 'run':
        print("You run away! Not without taking some change.")
        coin_update(35)
        l_escape()
    elif choice == 'fight':
        l_fight()
    else:
        print("Invalid Answer. Try Again..")
        l_darkpath()

def l_fight():
    print("You put your fists up and duke it out with the snake!")
    if strength >= 60:
        print("You take a rock and smash it over the snake's head crushing it! You've won and now have all the gold in the world to celebrate!")
        print("Congratulations! You completed Ending 7!\nEnding 7: You live life spoiled in the ultimate riches! Literal Jackpot!")
        print(f'Coins: {coins}')
        sys.exit()
    elif strength >= 20:
        print("The snake bites you, hard! You stagger then fall to the floor, venom coursing through your veins. It's over.")
        print("Congratulations! You completed Ending 8!\nEnding 8: You died. Consumed by the snake and dying with whatever dignity you had left.")
        print(f'Coins: {coins}')
        sys.exit()

def r_look():
    global choice
    print("You found 45 coins, a map, a sword, and some warm clothes.")
    coin_update(45)
    inventory.append("map") #I like the idea of user having an inventory and it being useful for later choices.
    inventory.append("clothes")
    inventory.append("sword")
    print("Inventory:", inventory)
    print("What will you do now?\n'Follow' the whispers\n'Go Right'\n'Go Back'")
    choice = input()
    if choice == 'follow':
        r_follow()
    elif choice == 'right':
        r_right()
    elif choice == 'go back':
        right()
    else:
        print("Invalid Answer. Try Again..")
        r_look()

def r_follow():
    global choice
    print("You follow the whispers, a light flickers dimly as the sounds get louder. You reach a cave room.")
    print("On the other side of the opening there's a small group of people.")
    print("They are skin and bones with thin hair and...dirty. You smell the faint twinge of blood in the air. Uh oh.")
    print("Their eyes lock on you. What will you do?\n'Run'!\n'Fight'!")
    choice = input()
    if choice == 'run':
        print("You start to back away, but trip. They reach you quickly, mouths salivating. Your fate has been sealed.")
        print("Congratulations! You completed Ending 9!\nEnding 9: You were torn apart and eaten. Brutal...")
        sys.exit()
    elif choice == 'fight':
        r_fight()
    else:
        print("Invalid Answer. Try Again..")
        r_follow()

def r_fight():
    if strength >= 55:
        print("You engage in a short battle with the biggest one. You kill him with your bare hands. You look towards the rest, they cower in fear.")
        print("They lead you down winding tunnels to an underground cave village. Here, they bring you in front of the Chief.")
        print("Congratulations! You completed Ending 10!\nEnding 10: You've become a renowned warrior amongst the cannibal tribe! You live amongst them as a protector.")
        print(f'Coins: {coins}')
        sys.exit()
    else:
        print("You put up a fight, but they overpower you. You do not have enough strength.")
        print("Congratulations! You completed Ending 9!\nEnding 9: You were torn apart and eaten. Brutal...")
        sys.exit()

def r_right():
    global choice
    print("You crawl into the small opening. You see a bit of white light peering through some leaves covering the other end.")
    if strength >= 30 and "clothes" in inventory:
        print("You escaped! It's a little chiller than you last remember it, but you'll survive.")
        print("Congratulations! You completed Ending 11!\nEnding 11: You wander a winter wonderland! With the map, you are equipped to explore this new world.")
        print(f'Inventory: {inventory}')
        print(f'Coins: {coins}')
        sys.exit()
    elif strength >= 30:
        print("You escaped! It's a little chiller than you last remember it. You don't get far before the cold reaches you.")
        print("Congratulations! You completed Ending 12!\nEnding 12: You die from hypothermia. Maybe you should've been a little more nosey...")
        print(f'Coins: {coins}')
        sys.exit()
    else:
        print("Uh oh! You've gotten stuck! It looks like you didn't have enough strength to make it through...")
        print("Congratulations! You completed Ending 13!\nEnding 13: You die, cold, alone, and in an odd position. The last thing on your mind is wonders of what could've been...")
        print(f'Coins: {coins}')
        sys.exit()

while True:
    adventure_start()
    play_again = input("Would you like to play again?\n'Yes' for restart\n'No' to end.").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break