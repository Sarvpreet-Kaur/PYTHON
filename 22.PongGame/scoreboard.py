from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.new_score()

    def new_score(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.lscore, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 210)
        self.write(self.rscore, align="center", font=("Courier", 50, "normal"))


    def score_to_l(self):
        self.lscore+=1
        self.new_score()

    def score_to_r(self):
        self.rscore+=1
        self.new_score()

    def winner(self,won):
        self.goto(0,0)
        if won=='l':
            win = self.lscore - self.rscore
            self.write(f"Left player won by {win}" ,align="center", font=("Courier", 25, "normal"))
        else:
            win = self.rscore - self.lscore
            self.write(f"Right player won by {win}", align="center", font=("Courier", 25, "normal"))
