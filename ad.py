import sys
import random
coins=0
strength= random.randint(10,100)
inventory=[]
choice= input()
def coin_update(sum):
    global coins
    coins+=sum 
def left():
    print("The tunnel leads to a stream. Follow it 'downstream' or 'upstream'?")
    choice
    while choice==('downstream'or 'Downstream'):
        print(l_downstream)
        if choice==('upstream'or'Upstream'):
            print(l_upstream)
        else:
            print("Invalid Answer. Try Again..")
            choice
        break
def right():
    print("You walk down the path to a small clearing.\nYou see the light coming from a hole at the top of the cave.")
    print("The whispers are still distant, but is now accompanied by a faint flickering light.\nTo the 'right', you see a small opening. Just enough for you to crawl through..")
    print("Would you like to 'look' around, 'follow' the whispers, or go 'right'") 
    choice
    while choice==('look'or 'Look'):
        print(r_look)
        if choice==('follow'or'Follow'):
            print(r_follow)
        elif choice==('right'or'Right'):
            print(r_right)
        else:
            print("Invalid Answer. Try Again..")
            choice
        break
def adventure_start():
    print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears.\n You have no memory of how you got here. As you get up and dust yourself off, you notice two paths ahead.")
    print("On your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water")
    print("On your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers echoing from within.")
    print("\nWhat will you decide?\n'Left'\n'Right'")
    choice
while choice==('left'or'Left'):
    print(left)
    if choice==('Right'or'right'):
        print(right)
    else:
        print("Invalid Answer. Try Again..")
        choice
    break
def l_climb():
    print("You get to the top successfully. You spot a slim opening where the light originates from. You squeeze through. Now outside, you see three young women standing on the side of the stream.")
    print("They notice you and begin to approach you. What will you do?\n 'Run'!\n 'Show' your coins")
    choice
    while choice==('Run'or'run'):
        print(l_run)
        if choice==('Show'or'show')and coins>=99:
            print("You are lead to a hidden village and brought in front of the Village Chief. Showing your riches, you are deemed a gift from the gods and are celebrated as such.")
            print("Congratulations! You completed Ending 1!\n Ending 1: You live a lavish life amongst the villagers.")
            print(f'Coins:{coins}')
        else:
            print("Invalid Choice. Try Again..")
            choice
        break
def l_downstream():
    print("Following the stream downstream, you reach a waterfall. How will you get down?\n 'Jump'?\n 'Look' Around?")
    choice
    while choice==('Jump'or'jump'):
        print("Wow! Such a brave soul!\n You jump, but unforunately hit your head on a rock upon impact.\n You died.")
        print("Congratulations! You completed Ending 4!\n Ending 4:\nYour spirit becomes bound to the small lake below, your job becomes warding off people from the teasures that lie close by.")
        print(f'Coins:{coins}')
        sys.exit()
        if choice==('Look'or'look'):
            print("You see a pattern of rocks along the wall to the left of the waterfall. It looks like a set of stairs. You try your luck and travel down.")
            print("After safely getting down, you see a dim light coming from a small tunnel across the lake, but something calls you towards a dark path to your left.")
            print("What will you decide?\n'Tunnel'\n 'Dark path'")
            choice
        else:
            print("Invalid Answer. Try Again..")
            choice
        break
    while choice==('tunnel'or'Tunnel'):
        print(l_escape)
        if choice==('Dark path'or'dark path'):
            print(l_darkpath)
        else:
            print("Invalid Answer. Try Again..")
            choice
        break
      
def l_upstream():
    print("You follow the stream upstream. You see something shiny flickering in the shallow water as you walk.\nWould you like to check it out?")
    print("Yes or No?")
    choice
    while choice==('yes'or'Yes'):
        coin_update(100)
        print("You found 100 coins!")
        print(f'Coins:{coins}')
        if choice==('no'or'No'):
            print("You have decided to keep going.")
        else:
            print("Invalid Choice. Try again..")
            choice
        break
    print("You continue upstream. It leads to a mildly steep cliffside where a dim light shines at the top.\nWill you 'Climb'up or 'Go Back'?")
    choice
    while choice==('climb'or'Climb'):
        print(l_climb)
        if choice==('go back'or'Go back'or'Go Back'):
            print(l_downstream)
        else:
            print("Invalid Answer. Try Again..")
        choice
        break

def l_run():
    print("You run! Soon you run straight into a village clearing. You are taken away by guards nearby and are presented in front of the Village Chief!")
    print("They speak in a foreign language around you. You are then nudged by spears closer to the Chief. What will you do?\n Say 'Nothing'\n 'Show' your coins")
    choice
    if choice==('Show'or'show')and coins>=99:
        print("You are spared. Without much to lose, you stick around and integrate yourself into their society.")
        print("Congratulations! You completed Ending 2!")
        print(f'Coins:{coins}')
        sys.exit()
    elif choice==('Nothing'or'nothing'):
        print("You've sealed your fate. You become sacrifice to their God of Protection. Cool Guy.")
        print("Congratulations! You completed Ending 3!")
        print(f'Coins:{coins}')
        sys.exit()
def l_escape():
    print("You escaped!")
    if coins<=30:
        print("Congratulations! You completed Ending 5!")
        print("Ending 5: You now travel aimlessly, trying to make a living. You don't have enough to integrate into nearby societies...")
        sys.exit()
    else:
        print("Congratulations! You completed Ending 6!")
        print("Ending 6: You live a humble life in a nearby kingdom. Yet, every day until death, you think about what could've been.")
        sys.exit()

def l_darkpath():
    print("The dark path leads you to a cave room filled with gold! You're rich!")
    print("Suddenly, you hear a hiss from one of the dark corners of the room. A poisonous snake! What will you do?\n 'Run'!\n 'Fight' with your bare hands!")
    choice
    if choice==('Run'or'run'):
        print("You run away! Not without taking some change.")
        coin_update(35)
        print(l_escape)
    elif choice==('Nothing'or'nothing'):
        print(l_fight)
def l_fight():
    print("You put your fists up and duke it out with the snake!")
    if strength>=60:
        print("You take a rock and smash it over the snakes head crushing it! You've won and now have all the gold in the world to celebrate!")
        print("Congratulations! You completed Ending 7!\nEnding 7: You live life spoiled in the ultimate riches! Literal Jackpot!")
        print(f'Coins:{coins}')
        sys.exit()
    elif strength>=20:
        print("The snake bites you, hard! You stagger then fall to the floor, venom coursing through your veins. It's over.")
        print("Congratulations! You completed Ending 8!\n Ending 8: You died. Consumed by the snake and dying with whatever dignity you had left.")
        print(f'Coins:{coins}')
        sys.exit()
def r_look():
    print("You found 45 coins, a map, a sword and some warm clothes.")
    coin_update(45)
    inventory.append("map")
    inventory.append("clothes")
    inventory.append("sword")
    print(inventory)
    print("What will you do now?\n 'Follow' the whispers\n Go 'Right\n 'Go Back'")
    choice
    while choice==('Follow'or'follow'):
        print(r_follow)
        if choice==('Right'or'right'):
            print(r_right)
        else:
            print("Invalid Answer. Try Again..")
        choice
        break
def r_follow():
    print("You follow the whispers, a light flickers dimly as the sounds get louder. You reach a cave room. On the other side of the opening there's a small group of people.")
    print("They are skin and bones with thin hair and...dirty. You smell the faint twinge of blood in the air. Uh oh.")
    print("Their eyes lock on you. They look like they haven't seen a meal in days. Their eyes go wide with newfound excitement. What will you do?")
    print("'Run'!\n'Fight'!")
    choice
    while choice==('run'or'Run'):
        print("You start to back away, but trip. They reach you quickly, mouths salvating. Your fate has been sealed.")
        print("Congratulations! You completed Ending 9!\n Ending 9: You were torn apart and eaten. Brutal...")
        sys.exit()
        if choice==('fight'or'Fight'):
            print(r_fight)
        else:
            print("Invalid Answer. Try Again..")
            choice
        break

def r_fight():
    if strength>=55:
        print("You engage in a short battle with the biggest one. You kill him with your bare hands. You look towards the rest, they cower in fear. One slowly approaches you and softly nudges you towards the entrance.")
        print("You follow. They lead you down winding tunnels to an underground cave village. Here, they bring you in front of the Chief, just as malnournished.")
        print("They exchange some grunts and words. The chief looks towards you and smile with brown teeth. You feel relief.")
        print("Congratulations! You completed Ending 10!\n Ending 10: You've become a renowned warrior amongst the cannibal tribe! You live amongst them as a protector. They're quite sweet when they respect you.")
        print(f'Coins:{coins}')
        sys.exit() 
    else:
        print("You put up a fight, but they end up overpowering you. You do not have enough strength.")
        print("Congratulations! You completed Ending 9!\n Ending 9: You were torn apart and eaten. Brutal...")
        print(f'Coins:{coins}')
        sys.exit()    

def r_right():
    print("You crawl into the small opening. You see a bit of white light peering through some leaves covering the other end.")
    if strength>=30 and ("clothes" in inventory):
        print("You escaped! It's a little chiller than you last remember it, but you'll survive.")
        print("Congratulations! You completed Ending 11!\n Ending 11: You wander a winter wonderland! With the map, you are equipped to explore this new world.")
        print(f'Inventory:{inventory}')
        print(f'Coins:{coins}')
        sys.exit()
    elif strength>=30:
        print("You escaped! It's a little chiller than you last remember it. You don't get far before the cold reaches you.")
        print("Congratulations! You completed Ending 12!\n Ending 12: You die from hypothermia. Maybe you should've been a little more nosey...")
        print(f'Coins:{coins}')
        sys.exit()
    else:
        print("Uh oh! You've gotten stuck! It looks like you didn't have enough strength to make it through...")
        print("Congratulations! You completed Ending 13!\n Ending 13: You die, cold, alone and in an odd position. The last thing on your mind is wonders of what could've been...")
        print(f'Coins:{coins}')
        sys.exit()

while True:
    adventure_start()
    play_again= input("Would you like to play again?\n'Yes' for restart\n 'No' to end.")
    if (play_again!='yes'or'Yes'):
        print("Thank you for playing!")
        break
