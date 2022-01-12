from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


pen = Turtle()
pen.width(3)
pen.speed("fastest")


def draw_spirograph(gap):
    for _ in range(360 // gap):
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(pen.heading() + gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
