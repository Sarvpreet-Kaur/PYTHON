print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.\n Your mission is to find the treasure")
ans = input("You want to go left or right? ")
if(ans == "left" or ans == "Left"):
    print('''You fell into hole.
     GAME OVER ''')
else:
    ans = input('''You are at the lake
    You want to 'wait' for the boat or 'swim' ''')

    if(ans == 'wait'):
        print("You are attacked by the pirates.\n GAME OVER")
    else:
        ans = input("Which door you want to choose 'red', 'blue' or 'yellow'? ")
        if(ans == 'red'):
            print("You are burnt\n GAME OVER")
        elif(ans == 'yellow'):
            print("You are eaten by sun\nGAME OVER")
        else:
            print("You WONNNN Treasure is yours")
