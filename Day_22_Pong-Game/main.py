from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from draw_line import Line
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # makes amination 0

# create paddles before update
paddle1 = Paddle(-387, 0)
paddle1.color("red")
paddle2 = Paddle(380, 0)
paddle2.color("blue")
ball = Ball()

# create new score board
scoreboard = Scoreboard()
# create line at center

line = Line()

game_is_on = True

while game_is_on:
    # update screen to avoid animation
    screen.update()

    # allow the ball to move while game is on
    ball.move()
    time.sleep(ball.move_speed)  # for speed purpose

    # Listen from screen
    screen.listen()

    screen.onkeypress(fun=paddle1.go_up, key="w")
    screen.onkeypress(fun=paddle1.go_down, key="s")
    screen.onkeypress(fun=paddle2.go_up, key="Up")
    screen.onkeypress(fun=paddle2.go_down, key="Down")

    # collision with top and bottom
    if ball.ycor() >= 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with paddle1 and paddle2 (Using distance with paddle)
    if ((ball.distance(paddle1) < 50 and ball.xcor() < -350) or
            (ball.distance(paddle2) < 50 and ball.xcor() > 350)):
        ball.bounce_x()
        ball.move_speed *= 0.9  # used in time (less is time, more is speed)

    if ball.xcor() < -380:
        # ball crosses player 1 section
        scoreboard.player2_score += 1
        scoreboard.update_score()
        ball.reset_position()

    if ball.xcor() > 380:
        # ball crosses player 2 section
        scoreboard.player1_score += 1
        scoreboard.update_score()
        ball.reset_position()  # also resets speed
