def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    steps = 0
    while not right_is_clear():
        move()
        steps += 1
    turn_right()
    move()
    turn_right()
    for x in range(steps):
        move()
    turn_left()

while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        jump()
