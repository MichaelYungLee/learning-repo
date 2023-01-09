from random import randint

import colorgram
from turtle import Screen, Turtle


def extract_colors_from_image(image_name, number_of_colors):
    extracted_colors = colorgram.extract(image_name, number_of_colors)
    rgb_colors = []
    for color in extracted_colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


def random_color(colors):
    return colors[randint(0, len(colors)-1)]


def main():
    colors = extract_colors_from_image('image.jpg', 30)
    x, y = -255, -255

    turtle = Turtle()
    turtle.speed(0)
    turtle.penup()
    turtle.setposition((x, y))
    turtle.hideturtle()

    screen = Screen()
    screen.colormode(255)

    for i in range(10):
        for j in range(10):
            position = (x + j*50, y + i*50)
            turtle.setposition(position)
            turtle.dot(20, random_color(colors))

    screen.exitonclick()


if __name__ == "__main__":
    main()