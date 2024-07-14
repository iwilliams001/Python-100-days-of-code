from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

entries = {}
for tim in colors:
    entries[tim] = Turtle(shape="turtle")
    entries[tim].color(tim)
    entries[tim].penup()
    pos = colors.index(tim)
    entries[tim].goto(-230, pos*30 - 80)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in entries:
        if entries[turtle].xcor() > 230:
            is_race_on = False
            winning_color = entries[turtle].pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        entries[turtle].forward(rand_distance)


screen.exitonclick()
