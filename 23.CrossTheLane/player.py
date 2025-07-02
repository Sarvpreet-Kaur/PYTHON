from turtle import Turtle

start_position = (0,-180)
class Player(Turtle):
    def __init__(self,mode):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1.1,stretch_len=1.1)
        self.penup()
        if mode=="dark":
            self.color("pink")
        else:
            self.color("blue")
        self.setheading(90)
        self.goto(start_position)

    def move_up(self):
        xcor = self.xcor()
        ycor = self.ycor() + 10
        self.goto(xcor,ycor)

    def move_left(self):
        xcor = self.xcor() - 10
        ycor = self.ycor()
        self.goto(xcor,ycor)

    def move_right(self):
        xcor = self.xcor() + 10
        ycor = self.ycor()
        self.goto(xcor,ycor)

    def new_level(self):
        self.goto(start_position)