import os
cls = lambda: os.system('cls')
#cls()
import random

def compare(guess):
    global game_over, attempts_left, target
    attempts_left -= 1
    if guess == target:
        game_over = True
        return f"You got it! The answer is {target}."
    elif guess < target:
        return "Too low."
    else:
        return "Too high."
    
def level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")[0].lower()
    if difficulty == "h":
        return 5
    else:
        return 10
    
def game():
    global game_over, attempts_left, target
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number from 1 to 100.")    
    attempts_left = level()
    target = random.choice(range(1,101))
    game_over = False
    while not game_over and attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print(compare(guess))
        if attempts_left == 0:
            game_over = True
            print(f"Game over. The number was {target}.")
    
new_game = True
while new_game:
    game()    
    try_again = input("Do you want to play again? Type 'yes' or 'no'. ")[0].lower()
    if try_again == "y":
        new_game = True
    else:
        new_game = False
    cls()