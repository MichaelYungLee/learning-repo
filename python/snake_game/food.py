from random import choice
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = choice(range(-280, 300, 20))
        random_y = choice(range(-280, 300, 20))
        self.goto((random_x, random_y))
