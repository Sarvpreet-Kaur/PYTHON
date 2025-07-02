from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up,"W")
screen.onkey(snake.down,"S")
screen.onkey(snake.left,"A")
screen.onkey(snake.right,"D")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_score()

    #Detect collision with wall
    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>270:
        snake.reset()
        scoreboard.reset()

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()