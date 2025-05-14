
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print('''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
''')

print("Welcome to ONLINE CALCULATOR")

work = input("Click yes to continue with calculator and no to exit: ")
prev = 'n'
ans = 0
while work == 'yes':
    invalid = False
    if prev=='y':
        first = ans
    else:
        first = int(input("Enter first number: "))
    operation = input("Select the operation -\n+\n-\n*\n/\n")
    second = int(input("Enter second number: "))

    if operation=='+':
        ans = add(first,second)
    elif operation=='-':
        ans = sub(first,second)
    elif operation=='*':
        ans = mul(first,second)
    elif operation=='/':
        ans = div(first,second)
    else:
        invalid = True
        print("Invalid operation")

    if invalid == False:
        print(f"{first} {operation} {second} = {ans}")
    prev = input("Do you want to work with prev. Type y for yes and n for no: ")
    if prev == 'n':
        work = input("Click yes to continue with calculator and no to exit: ")