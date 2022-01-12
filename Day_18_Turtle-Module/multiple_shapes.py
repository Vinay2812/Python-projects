import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
pen = Turtle()
pen.width(10)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(100)
        pen.right(angle)


for sides in range(3, 11):
    pen.color(random_color())
    draw_shape(sides)

screen = Screen()
screen.exitonclick()
