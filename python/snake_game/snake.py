from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.body = []
        for i in range(3):
            x, y = 0 - (20*i), 0
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setposition((x,y))
            self.body.append(segment)
        self.head = self.body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        current_segment = self.body[0]
        current_position = current_segment.position()
        current_segment.forward(MOVE_DISTANCE)
        for next_segment in self.body[1:]:
            next_position = next_segment.position()
            next_segment.setposition(current_position)
            current_position = next_position