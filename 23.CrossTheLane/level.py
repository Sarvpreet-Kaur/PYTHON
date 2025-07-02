from turtle import Turtle

class Level(Turtle):
    def __init__(self,mode):
        super().__init__()
        self.penup()
        self.hideturtle()
        if mode=="dark":
            self.color("white")
        self.goto(-290,170)
        self.level = 1
        self.board()

    def board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 15, "normal"))

    def next_level(self):
        self.level +=1
        self.board()

    def game_over(self):
        self.goto(-40,0)
        self.write(f"Level: {self.level}\nGAME OVER", align="left", font=("Arial", 15, "normal"))

        