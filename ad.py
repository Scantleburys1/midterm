import sys
coins=0
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
