from turtle import Turtle

move_distance = 20
Up = 20
Down = -20
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("pink")
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_wid=5,stretch_len=1)

    def up(self):
        x = self.xcor()
        y = self.ycor() + Up
        self.goto(x,y)

    def down(self):
        x = self.xcor()
        y = self.ycor() + Down
        self.goto(x, y)


