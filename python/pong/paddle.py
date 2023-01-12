from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setposition(position)

    def move_up(self):
        if self.ycor() + 20 < 250:
            self.sety(self.ycor()+20)

    def move_down(self):
        if self.ycor() - 20 > -250:
            self.sety(self.ycor()-20)