from turtle import Turtle

with open("data.txt") as data:
    highest = int(data.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 285)
        self.score = 0
        self.high_score = highest
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", False, align="center",
                   font=('Arial', 10, 'normal'))

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:
                new_data.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()
