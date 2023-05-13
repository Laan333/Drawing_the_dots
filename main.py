from turtle import Pen, Screen
from random import choice

import took_colors_from_the_painting

pen = Pen()
screen = Screen()
screen.setup(530, 520)
screen.colormode(255)
x_coord = -230
y_coord = -250


def randomed_color():
    list_of_colors = took_colors_from_the_painting.took_colors("ss.jpg", 55)
    random_color = choice(list_of_colors)
    if random_color == (255, 255, 255):
        list_of_colors.remove(random_color)
        randomed_color()
    return random_color


def place():
    pen.speed(0)
    global y_coord
    pen.up()
    pen.goto(x_coord, y_coord)
    pen.down()

    for i in range(10):
        random_colors = randomed_color()
        pen.fillcolor(random_colors)
        pen.color(random_colors)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.up()
        pen.forward(50)
        pen.down()
    y_coord += 50


for i in range(10):
    place()

screen.exitonclick()
