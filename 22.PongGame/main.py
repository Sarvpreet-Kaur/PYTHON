import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)
 
line = Turtle()
line.hideturtle()
line.color("white")
line.pensize(5)
line.color("black")
line.goto(0,400)
line.right(90)

count = 20
while count>0:
    line.forward(20)
    line.color("white")
    line.forward(20)
    line.color("black")
    count-=1

scoreboard = Scoreboard()
r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
x = 10
y = 10
screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

screen.onkey(r_paddle.up,"o")
screen.onkey(r_paddle.down,"k")

game = True
while game:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move()

    if ball.ycor() >278 or ball.ycor()<-278:
        ball.bounce()

    if (ball.xcor() > 340 or ball.xcor() < -340) and (r_paddle.distance(ball)<50 or l_paddle.distance(ball)<50):
        print("Made contact")
        ball.paddle_bounce()

    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.score_to_l()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.score_to_r()

    if scoreboard.lscore==5:
        game = False
        line.clear()
        scoreboard.winner("l")

    if scoreboard.rscore==5:
        game = False
        line.clear()
        scoreboard.winner("r")






screen.exitonclick()