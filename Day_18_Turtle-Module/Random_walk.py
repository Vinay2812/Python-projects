import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
pen = Turtle()
pen.width(10)
pen.speed("fastest")


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


direction = [0, 90, 180, 270]


def random_walk():
    move = random.choice(direction)
    pen.forward(30)
    pen.setheading(move)


for _ in range(200):
    pen.color(random_color())
    random_walk()

screen = Screen()
screen.exitonclick()
