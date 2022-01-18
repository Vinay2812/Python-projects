from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    # to write score
    def update_score(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"{self.player1_score} {self.player2_score}",
                   align="center", font=("Courier", 80, "normal"))
