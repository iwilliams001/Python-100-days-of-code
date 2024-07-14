from turtle import Turtle, Screen
import random

my_colors = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
             (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
             (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
             (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(1)
tim.speed(0)
tim.hideturtle()
for i in range(10):
    tim.penup()
    tim.goto(-200, -200 + i*50)
    for j in range(10):
        tim.dot(20, random.choice(my_colors))
        tim.forward(50)

screen.exitonclick()
