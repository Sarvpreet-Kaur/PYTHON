import random
import turtle as t


tillu  = t.Turtle()
tillu.shape("turtle")
tillu.color("coral3")
t.colormode(255)
# count = 4
# while count>0:
#     tillu.forward(100)
#     tillu.right(90)
#     count-=1
#
# count = 5
# while count>0:
#     tillu.forward(10)
#     tillu.color("white")
#     tillu.forward(10)
#     tillu.color("coral2")
#     count-=1
#
# tillu.left(90)
# count = 5
#
# while count > 0:
#     tillu.forward(10)
#     tillu.penup()
#     tillu.forward(10)
#     tillu.pendown()
#     count -= 1
#
# tillu.left(90)
# colors = ['red','yellow','blue','orange','green','pink','purple','blue','cyan','golden']
# for i in range(3,11):
#     size = 4*i
#     count = i
#     angle = 360/i
#     tillu.color(random.choice(colors))
#     while count>0:
#         tillu.forward(size)
#         tillu.right(angle)
#         count-=1
#
# colors = ["tomato","medium purple","lime green","cornflower blue"]
# directions = ["north","south","east","west"]
# count = 100
# tillu.pensize(5)
# tillu.speed("fastest")
# while count>0:
#     dir = random.choice(directions)
#     color_ = random.choice(colors)
#     tillu.forward(20)
#     tillu.color((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
#     if dir == "east":
#         tillu.right(0)
#     elif dir == "north":
#         tillu.right(90)
#     elif dir == "south":
#         tillu.right(270)
#     else:
#         tillu.right(180)
#     count-=1
tillu.color((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
tillu.speed("fastest")
curr = tillu.heading()
while curr<=360:
    tillu.circle(100)
    tillu.color((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
    tillu.setheading(curr)
    curr+=3

screen = t.Screen()
screen.exitonclick()