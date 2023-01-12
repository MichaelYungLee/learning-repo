import random
import time
from turtle import mode, Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

def main():
    mode("logo")
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    ball = Ball()
    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))
    scoreboard = Scoreboard((0, 250))
    game_is_on = True

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")
    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ((ball.xcor() > 330 and ball.distance(right_paddle) <= 50) or
            (ball.xcor() < -330 and ball.distance(left_paddle) <= 50)):
            ball.bounce_x()
            ball.increase_speed()

        # Detect collision with sides
        if ball.xcor() > 380 or ball.xcor() < -380:
            scoreboard.add_point('left') if ball.xcor() > 380 else scoreboard.add_point('right')
            ball.reset()

        scoreboard.update_scoreboard()

    screen.exitonclick()

if __name__ == "__main__":
    main()