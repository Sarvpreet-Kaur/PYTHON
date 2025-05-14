import random

rock = ''' 
   --------
___'  _____)
      (______)
      (______)
      (_____)
---.__(___)
'''

paper = '''
   --------
___'  _____)___
      (__________)
      (__________)
      (_________)
---.__(_______)
'''

scissors = '''
   --------
___'  _____)
      (_________)
      (_________)
      (_____)
---.__(___)
'''
GAME = [rock,paper,scissors]
print("Welcome to ROCK PAPER SCISSORS Game")

user = int(input("Choose 0 for ROCK, 1 for PAPER ans 2 for SCISSORS "))
print("Your choice  - ")
print(GAME[user])

computer = random.randint(0,2)
print("Computer choice  - ")
print(GAME[computer])


if user==computer:
    print("DRAW")
elif user==0 and computer==1:
    print("COMPUTER WON")
elif user==0 and computer==2:
    print("YOU WON")


if user==1 and computer==0:
    print("YOU WON")
elif user==1 and computer==2:
    print("COMPUTER WON")

if user==2 and computer==1:
    print("YOU WON")
elif user==2 and computer==0:
    print("COMPUTER WON")

