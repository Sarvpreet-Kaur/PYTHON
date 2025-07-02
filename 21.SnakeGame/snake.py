from turtle import Turtle

st_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for pos in st_positions:
            self.add_segment(pos)

    def add_segment(self,pos):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(pos)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create()
        self.head = self.segments[0]