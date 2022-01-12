import turtle

pen = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def turn_left():
    pen.setheading(pen.heading() - 10)


def turn_right():
    pen.setheading(pen.heading() + 10)


def clear():
    pen.clear()
    pen.up()
    pen.home()
    pen.down()


screen.listen()
screen.onkey(fun=move_forward, key="Right")
screen.onkey(fun=turn_left, key="Down")
screen.onkey(fun=turn_right, key="Up")
screen.onkey(fun=move_backward, key="Left")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
