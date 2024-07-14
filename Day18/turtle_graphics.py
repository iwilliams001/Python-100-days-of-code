from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.pensize(1)
tim.speed(0)
for i in range(100):
    tim.pencolor(random_color())
    tim.right(3.6)
    tim.circle(100)

# for x in range(3, 11):
#     tim.pencolor(random.randint(0, 255),
#                  random.randint(0, 255),
#                  random.randint(0, 255))
#     angle = 360/x
#     for i in range(x):
#         tim.forward(100)
#         tim.right(angle)


screen.exitonclick()
