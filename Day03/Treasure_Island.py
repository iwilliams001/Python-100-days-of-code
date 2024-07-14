## Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first = input('You are at a crossroad. Where do you want to go?\nType "left" or "right".')
first = first.lower()
if first == "left":
    second = input('You come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat or type "swim" to swim across.')
    second = second.lower()
    if second == "wait":
        colour = input('You arrive at the island unharmed.There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?')
        colour = colour.lower()
        if colour == "yellow":
            print("You win!")
        elif colour == "red":
            print("You were burned by fire.\nGame Over.")
        elif colour == "blue":
            print("You were eaten by beast.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("You were attacked by a trout.\nGame Over.")

else:
    print("You fell into a hole.\nGame Over.")



