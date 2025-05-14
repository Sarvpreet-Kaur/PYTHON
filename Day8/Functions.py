def greet():
    print("Hello")
    print("Namaste")
    print("SatSriAkal")

greet()

def greetName(name):
    print(f"Hello {name}")
    print(f"How are you {name}?  ")

greetName("Reet")

def add(a,b=10):
    print (a+b)
add(5)

def addA(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

addA(1,2,3,4,5)

def addK(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum += value
        print(f"{key}:{sum}")
    print(sum)

addK(a=1,b=2,c=3,d=4,e=5)

