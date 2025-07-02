from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.high_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  Highest Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"      Score: {self.score}\n GAME OVER.", move=False, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_score()


