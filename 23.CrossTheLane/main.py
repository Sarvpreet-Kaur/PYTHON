import time
from turtle import Screen
from player import Player
from cars import Cars
from level import Level

screen = Screen()
screen.setup(600,400)

mode = screen.textinput(title="PLAY MODE" ,prompt = "Choose your mode: dark or light")
if mode=="dark":
    screen.bgcolor("black")

screen.tracer(0)
player = Player(mode)
cars = Cars()
level = Level(mode)
screen.listen()

screen.onkey(player.move_up,"Up")
screen.onkey(player.move_right,"Right")
screen.onkey(player.move_left,"Left")

game = True

screen.title("CROSS THE LANE")
count = 0
while game:

    time.sleep(cars.moving_speed)
    screen.update()

    count+=1

    if count%20 == 0:
        cars.create()
        count = 0
    # cars.move()

    for car in cars.all_cars:
        if car.distance(player)<= 20:
            cars.hit()
            level.game_over()
            game = False

    if player.ycor()>=190:
        player.new_level()
        cars.increase_speed()
        level.next_level()

    cars.move()



screen.exitonclick()
