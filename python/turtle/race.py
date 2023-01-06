from random import randint
from turtle import Screen, Turtle


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class RacingTurtle(Turtle):
    def __init__(self, color, starting_position):
        super().__init__(shape="turtle")
        self.color(color)
        self.penup()
        self.goto(starting_position)

    def move_random_distance_forward(self):
        self.forward(randint(0,10))


def setup_race():
    racing_turtles = {}
    starting_x, starting_y = -230, -100
    for color in colors:
        racing_turtles[color] = RacingTurtle(color, (starting_x,starting_y))
        starting_y += 40
    return racing_turtles


def determine_winner(racing_turtles):
    for turtle in racing_turtles:
        if racing_turtles[turtle].position()[0] > 230:
            winner = turtle
    return winner

def main():
    screen = Screen()
    screen.setup(width=500, height=400)

    user_bet = None
    while user_bet not in colors:
        user_bet = screen.textinput(
            title="Make your bet", 
            prompt="Which turtle will win the race? Enter a color: "
        ).lower()

    racing_turtles = setup_race()
    is_race_on = True    


    while is_race_on:
        for turtle in racing_turtles.values():
            turtle.move_random_distance_forward()

            if turtle.position()[0] > 230:
                is_race_on = False

    winner = determine_winner(racing_turtles)

    if user_bet in winner:
        print(f"You've won! The {winner} turtle is the winner!")
    else:
        print(f"You've lost. The {winner} turtle is the winner.")
    
    screen.exitonclick()

if __name__ == "__main__":
    main()