from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -300)
        self.setheading(to_angle=90)

        while(self.ycor() < 300):
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(10)
