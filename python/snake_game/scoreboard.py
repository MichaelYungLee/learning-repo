from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto((0, 260))

        self.score = 0
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self, num):
        self.score += num

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
