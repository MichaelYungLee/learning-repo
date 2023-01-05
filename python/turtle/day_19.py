from turtle import Screen, Turtle


def process_input(turtle, btn):
    match btn:
        case 'c':
            clear(turtle)
        case 'w':
            move_forward(turtle)
        case 's':
            move_backward(turtle)
        case 'a':
            turn_left(turtle)
        case 'd':
            turn_right(turtle)
        case _:
            pass

def move_forward(turtle):
    turtle.forward(10)

def move_backward(turtle):
    turtle.backward(10)

def turn_left(turtle):
    turtle.left(10)

def turn_right(turtle):
    turtle.right(10)

def clear(turtle):
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def main():
    turtle = Turtle()
    screen = Screen()

    screen.listen()

    screen.onkeypress(lambda t=turtle,b='c': process_input(t, b), 'c')
    screen.onkeypress(lambda t=turtle,b='w': process_input(t, b), 'w')
    screen.onkeypress(lambda t=turtle,b='s': process_input(t, b), 's')
    screen.onkeypress(lambda t=turtle,b='a': process_input(t, b), 'a')
    screen.onkeypress(lambda t=turtle,b='d': process_input(t, b), 'd')

    screen.exitonclick()


if __name__ == "__main__":
    main()