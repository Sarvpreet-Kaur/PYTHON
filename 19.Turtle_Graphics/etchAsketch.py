from turtle import Turtle,Screen


tillu = Turtle()
screen = Screen()

def moveF():
    tillu.forward(10)
def moveB():
    tillu.backward(10)
def moveR():
    tillu.right(10)
def moveL():
    tillu.left(10)

def clear():
    tillu.clear()


screen.listen()
screen.onkey(moveF,"f")
screen.onkey(moveB,"b")
screen.onkey(moveL,"l")
screen.onkey(moveR,"r")
screen.onkey(clear,"c")



screen.exitonclick()