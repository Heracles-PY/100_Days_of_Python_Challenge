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
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input("You're at a cross road. Where you you want to go? Type 'left' or 'right'.").lower()

if first_choice == "right":
    print("You fell into a hole. Game over")
elif first_choice == "left":
    second_choice = input("You come to a lake with an island with a castle on it in the middle. Do you want to swim or wait for a boat? Type 'swim' or 'wait'.").lower()
    if second_choice == "swim":
        print("You get attacked by a giant fish and die. Game over.")
    elif second_choice == "wait":
        print("A boat arrives and takes you to the island.")
        third_choice = input("There are three doors on the castle. Choose red, blue, or yellow").lower()
        if third_choice == "red":
            print("The room is full of fire. Game over.")
        elif third_choice == "blue":
            print("A burst of cold air hits you. Game over.")
        else:
            print("You found the treasure! You win!")
else:
    print("Invalid input. Please choose again.")