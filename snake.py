from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE_MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.parts = []
        self.make_snake()
        self.head = self.parts[0]

    def make_snake(self):
        for snake_position in STARTING_POSITION:
            self.add_parts(snake_position)

    def add_parts(self, snake_position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(snake_position)
        self.parts.append(snake_part)

    def extend(self):
        self.add_parts(self.parts[-1].position())

    def move(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[part_num - 1].xcor()
            new_y = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(new_x, new_y)
        self.parts[0].forward(DISTANCE_MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
