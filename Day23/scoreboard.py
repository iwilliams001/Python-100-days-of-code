from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("black")
        self.score = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.goto(-170, 270)
        self.write(f"Level: {self.score}", align="center", font=FONT)
