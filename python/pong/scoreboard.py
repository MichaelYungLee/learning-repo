from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 72, 'normal')


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.setposition(position)

        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def add_point(self, player):
        if player == 'left':
            self.left_score += 1
        else:
            self.right_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
