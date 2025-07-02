import random
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
ans = random.randint(1,100)
chances = ""
if difficulty=='easy':
    chances = 10
else:
    chances = 5

print(f"You have {chances} attempts to guess the number ")
win = ""
while chances>0:
    number = int(input("Make a guess: "))
    if number >ans:
        print("Higher than correct answer")
        chances-=1
        print(f"You have {chances} attempts remaining to guess the number ")
    elif number == ans:
        print("On the SPOT.")
        win = True
        break
    else:
        print("Lower than correct answer")
        chances-=1
        print(f"You have {chances} attempts remaining to guess the number ")

if win==True:
    print("YOU WON")
else:
    print(f"Answer was {ans}. TOO CLOSE")
    print("You LOST THE GAME> BETTER LUCK NEXT TIME")