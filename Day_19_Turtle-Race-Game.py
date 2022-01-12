import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(
    title="Make a bet", prompt="Which turtle will win the race? Enter the color : "
)

colors = ["red", "orange", "green", "yellow", "blue", "purple"]
turtle_list = []

x = -215
y = -120

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(color, color)
    new_turtle.goto(x, y)
    y += 50
    turtle_list.append(new_turtle)

race_is_on = False
if user_guess:
    race_is_on = True

winner = ""
while race_is_on:
    for i, player in enumerate(turtle_list):
        if player.xcor() > 225.0:
            winner = colors[i]
            race_is_on = False
            break
        distance = random.randint(0, 10)
        player.forward(distance)


if user_guess == winner:
    print(f"Congratultion!! {winner} has won.")
else:
    print(f"Sorry {winner} has won.")

screen.exitonclick()
