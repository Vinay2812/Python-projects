from turtle import Turtle, Screen


pen = Turtle()
pen.color("red")
pen.speed("slow")

for _ in range(0, 4):
    pen.forward(100)
    pen.left(90)


screen = Screen()
screen.exitonclick()
