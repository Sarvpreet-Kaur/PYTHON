import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
    ,'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
    , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','&','*','(',')','^','%','+','-']

print("Welcome to Password Generator")
noOfChar = int(input("How many number of characters you want in your password? \n"))
noOfNum = int(input("How many numbers you want in your password? \n"))
noOfSym = int(input("How many number of symbols you want in your password? \n"))
password = ''

characters = [letters,numbers,symbols]
for num in range(1,noOfChar+1):
    temp = random.randint(0,2)
    if temp==1 and noOfNum!=0:
        password = password+(random.choice(characters[temp]))
        noOfNum = noOfNum-1
    elif temp==2 and noOfSym!=0:
        password = password + (random.choice(characters[temp]))
        noOfSym = noOfSym-1
    else:
        password = password + (random.choice(characters[temp]))

print(f"Your password is {password}")