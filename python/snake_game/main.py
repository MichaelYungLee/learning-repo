import time
from turtle import Screen, Turtle

from snake import Snake


def main():
    screen = Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    game_is_on = True

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()