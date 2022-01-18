from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("orange")
        self.shapesize(1.3)
        self.x_move_forward = 10
        self.y_move_forward = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move_forward
        new_y = self.ycor() + self.y_move_forward
        self.goto(new_x, new_y)

    def bounce_y(self):
        # to move in opposite direction from top and bottom
        self.y_move_forward *= -1

    def bounce_x(self):
        self.x_move_forward *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
