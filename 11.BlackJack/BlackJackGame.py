import random


cards = '''
                                      .------. _     _            _                ___
                   .------.           |A .   || |   | |          | |   (_)         | | 
                   |A_  _ |    .------; / \  || |__ | | __ _  ___| | ___  __ _  ___| | ___ 
                   |( \/ )|-----. _   |(_,_) || '_ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ / 
                   | \  / | /\  |( )  |  I  A|| |_) | | (_| | (__|   < | | (_| | (__|   <
                   |  \/ A|/  \ |_x_) |------'|_.__/|_|\__,_|\___|_|\_ | |\__,_|\___|_|\_\ 
                   `-----+'\  / | Y  A|                              ,_/ | 
                         |  \/ A|-----'                              |__/      
                         `------'
'''

print( cards )

space = "                                "
space2 = "                            "
print(f"{space}Welcome to BlackJack Game:\n {space2}Rules of the game are as follows: ")
print(f''' 
        Goal: Get a hand total closer to 21 than the dealer without going over (busting).
        Card Values: Number cards are face value; face cards are worth 10; Aces are worth 1 or 11.
        Gameplay: Players and dealer get 2 cards; players can Hit, Stand.
        Winning & Payouts: 1. Higher hand than dealer (without busting) wins 1:1.
                           2. Blackjack (Ace + 10) \n''')


cards = [1,2,3,4,5,6,7,8,9,10,11]
player = list()

for i in range(2):
    x = random.choice(cards)
    total = sum(player)
    if x==1 and total<10:
        x=11
    elif x==11 and total>=11:
        x=1
    player.append(x)

print(f"Your cards are {player} and the total is: {sum(player)}")
dealer = [random.choice(cards)]
print(f"Computer cards are: {dealer}")
lostP = False
winD = False
play = input("If you want to hit enter y else n: ").lower()


while play == 'y':
    x = random.choice(cards)
    #print(x)
    total = sum(player)

    if x == 1 and total < 10:
        x = 11
    elif x == 11 and total >= 11:
        x = 1

    player.append(x)

    total = sum(player)
    if total>21:
        lostP = True
        break

    print(f"Your cards are {player} and the total is: {sum(player)}")
    play = input("If you want to hit enter y else n: ").lower()

if not lostP :
    while sum(dealer)<=sum(player) and sum(dealer)<=21:
        x = random.choice(cards)
        #print(x)
        total = sum(dealer)

        if x == 1 and total < 10:
            x = 11
        elif x == 11 and total >= 11:
            x = 1

        dealer.append(x)

        if sum(dealer)==21:
            lostP = True
            break
        elif sum(dealer)>sum(player) and sum(dealer)<21:
            lostP = True
            break


if  lostP==True:
    if(sum(player)>21):
        print("You Went Over")
    else:
        print("Computer have more points than you")
    print("You Lost")

if lostP==False and winD==True:
    print("DRAW")

if lostP==False:
    print("YOU WIN")

print(f"Your cards are {player} and the total is: {sum(player)}")
print(f"Computer cards are {dealer} and the total is: {sum(dealer)}")
