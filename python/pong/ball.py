from random import choice, randint
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.set_random_heading()
        self.move_speed = 0.05

    def move(self):
        self.forward(10)

    def bounce_y(self):
        self.setheading(180-self.heading())

    def bounce_x(self):
        self.setheading(360-self.heading())

    def set_random_heading(self):
        heading = choice((randint(15, 165), randint(195, 345)))
        self.setheading(heading)

    def reset(self):
        self.home()
        self.set_random_heading()
        self.move_speed = 0.05

    def increase_speed(self):
        self.move_speed *= 0.8
