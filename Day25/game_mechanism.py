from turtle import Turtle


class StateOnMap(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

    def write_down(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", False, align="center", font=('Arial', 10, 'normal'))

    def update_score(self):
        self.score += 1
