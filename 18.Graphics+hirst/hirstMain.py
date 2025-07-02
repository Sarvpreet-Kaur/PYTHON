import random

import colorgram
from turtle import Turtle,Screen

colors = colorgram.extract('hirstImage.jpg',10)
rgb = []
for color in colors:
    rgb.append(((color.rgb.r),(color.rgb.g),(color.rgb.b)))
print(rgb)

tillu = Turtle()
tillu.screen.colormode(255)
tillu.penup()
x = -150
y = -100
tillu.goto(x,y)

for i in range(10):
    for j in range(10):
        tillu.pendown()
        tillu.dot(20,random.choice(rgb))
        tillu.penup()
        tillu.forward(30)
    y+=30
    tillu.goto(x,y)


screen = Screen()
screen.exitonclick()

