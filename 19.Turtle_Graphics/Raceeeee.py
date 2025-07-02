import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(500,500)

line = Turtle()
line.penup()
line.goto(200,200)
line.right(90)
line.pendown()
line.forward(350)
line.hideturtle()
user = screen.textinput(title="MAKE YOUR BET",prompt="Which turtle will win: ")
color = ['pink','coral','blue','green','grey']
all = []
y = -50
for i in range(5):
    tillu = Turtle()
    tillu.shape("turtle")
    tillu.penup()
    tillu.color(color[i])
    tillu.goto(-200, y+(i*30))
    all.append(tillu)

race = False
if user:
    race = True

while race:
    for turtle in all:
        if turtle.xcor() >200:
            race = False
            color = turtle.pencolor()
            if user==color:
                print(f"You WONNN!! {color} is the winner")
            else:
                print(f"You LOST!! {color} is the winner")
        dist = random.randint(0,10)
        turtle.forward(dist)

screen.exitonclick()