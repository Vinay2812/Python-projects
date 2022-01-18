
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x_pos, y_pos)

    def go_up(self):
        if self.ycor() < 243:
            self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor()-20)
