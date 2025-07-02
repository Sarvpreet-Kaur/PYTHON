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
tillu.speed("fastest")
tillu.penup()
tillu.hideturtle()

tillu.setheading(225)
tillu.forward(300)
tillu.setheading(0)

dots = 100
for dot in range(1,dots+1):
    tillu.dot(30,random.choice(rgb))
    tillu.forward(30)

    if dot%10==0:
        tillu.setheading(90)
        tillu.forward(30)
        tillu.setheading(180)
        tillu.forward(300)
        tillu.setheading(0)



screen = Screen()
screen.exitonclick()

