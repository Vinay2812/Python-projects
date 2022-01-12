import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)
pen = Turtle()
# pen.width(10)
pen.speed("fastest")
# colors = colorgram.extract("Day_18_Turtle-Module\dots-painting.jpg", 25)

color_list = [
    (237, 224, 80),
    (205, 4, 73),
    (236, 50, 130),
    (198, 164, 8),
    (111, 179, 218),
    (204, 75, 12),
    (219, 161, 103),
    (234, 224, 4),
    (11, 23, 63),
    (29, 189, 111),
    (22, 107, 174),
    (16, 28, 177),
    (216, 134, 179),
    (8, 186, 216),
    (229, 167, 200),
    (210, 25, 148),
    (122, 190, 160),
    (7, 49, 26),
    (34, 136, 72),
    (63, 20, 7),
    (126, 219, 234),
]

# for color in colors:
#     color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(color_list)


def random_color():
    return random.choice(color_list)


screen = Screen()

pen.up()
pen.goto(-250, -200)
pen.down()
for _ in range(10):
    for _ in range(10):
        pen.up()
        pen.goto(pen.xcor() + 40, pen.ycor())
        pen.dot(25, random_color())
        pen.down()
    pen.up()
    pen.goto(-250, pen.ycor() + 40)
    pen.down()


screen.exitonclick()
