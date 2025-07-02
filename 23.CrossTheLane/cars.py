import random
from turtle import Turtle,colormode

distance = 5
colormode(255)
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.moving_speed = 0.1

    def create(self):
        new_car = Turtle("square")
        new_car.color((random.randint(5,200),random.randint(5,200),random.randint(5,200)))
        new_car.penup()
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.moving_speed = self.moving_speed
        new_car.goto((280,random.randint(-130,130)))
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(distance)

    def increase_speed(self):
        for car in self.all_cars:
            car.moving_speed *= 0.7

    def hit(self):
        for car in self.all_cars:
            car.moving = 0


