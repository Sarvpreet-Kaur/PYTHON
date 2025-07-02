##SCOPES -

#1.Local Scope
enemies = 1

def increase_enemies():
    enemies = 2 
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")

#2.Enclosing Scope
def outer():
    y = 20
    def inner():
        print(f"Enclosed {y}")
    inner()
outer()

#3.Global Scope - can be accessed anywhere

### No Block Scope in Python
# if True:
#     inn = 20
# print(f"inn is inner if block and getting printed outside {inn}")

#Modifying global variable
enemies=1
def increase(enemies):
    #Using global variable makes it easy to fail
    # global enemies
    # enemies+=1
    return enemies+1
print(f"Enemies - {enemies}")

 #nonlocal variable
def outer():
    y = 3
    def inner():
        nonlocal y  # refers to y in the enclosing outer() function
        y = 7
        print("Inner y:", y)
    inner()
    print("Outer y:", y)
outer()
x = 100

def show():
    y = 200
    print("Globals:", globals().keys())
    print("Locals:", locals().keys())

show()

# NameSpaces
ree = 10  # Global namespace

def greet():
    print("Hello")  # 'greet' is also stored in the global namespace

class MyClass:
    pass  # 'MyClass' becomes part of the global namespace



def show_namespace():
    y = 99
    print("Local Namespace:", locals())  # Only local names
    print("Global Namespace:", globals())  # All global names

show_namespace()
