from turtle import Turtle, Screen

pen = Turtle()

for _ in range(10):
    pen.color("black")
    pen.penup()
    pen.forward(10)
    pen.pendown()
    pen.forward(10)

screen = Screen()
screen.exitonclick()
