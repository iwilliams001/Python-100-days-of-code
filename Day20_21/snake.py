from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        facing = self.head.heading()
        if facing == 0:
            self.head.left(90)
        elif facing == 180:
            self.head.right(90)
        else:
            pass

    def down(self):
        facing = self.head.heading()
        if facing == 0:
            self.head.right(90)
        elif facing == 180:
            self.head.left(90)
        else:
            pass

    def left(self):
        facing = self.head.heading()
        if facing == 90:
            self.head.left(90)
        elif facing == 270:
            self.head.right(90)
        else:
            pass

    def right(self):
        facing = self.head.heading()
        if facing == 90:
            self.head.right(90)
        elif facing == 270:
            self.head.left(90)
        else:
            pass
