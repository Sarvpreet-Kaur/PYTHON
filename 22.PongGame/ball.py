from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.xmove = self.start()
        self.ymove = self.start()
        self.moving_speed = 0.1

    def start(self):
        return random.randint(1,10)

    def move(self):
        new_x = self.xcor()+ self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1
        self.moving_speed *= 0.7

    def reset_position(self):
        self.goto(0,0)
        self.paddle_bounce()
        self.moving_speed = 0.1
