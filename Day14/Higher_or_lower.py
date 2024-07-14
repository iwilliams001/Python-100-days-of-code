import os
cls = lambda: os.system('cls')
#cls()
import random
from game_data import data

highest_score = 0
## Determine article (a or an)
def article(text):
    vowels = ["a","e","i","o","u"]
    if text[0].lower() in vowels:
        return "an"
    else:
        return "a"
    
## Randomly fetch an element from the list without including the previous two
def fetch(indices):
    new_list = []
    for x in range(len(data)):
        new_list.append(x)

    a = indices[0]
    b= indices[1]
    indices.remove(indices[0])
    c =random.choice(new_list)
    while c == a or c == b:
        c =random.choice(new_list)
    indices.append(c)
    return indices
    
## Text to be displayed
def display(indices):
    print(f"Compare A: {data[indices[0]]["name"]}, {article(data[indices[0]]["description"])} {data[indices[0]]["description"]}, from {data[indices[0]]["country"]}.\n\nVS\n\nAgainst B: {data[indices[1]]["name"]}, {article(data[indices[1]]["description"])} {data[indices[1]]["description"]}, from {data[indices[1]]["country"]}.\n")

    return input("Who has more followers? Type 'A' or 'B': ").lower()
    
## Keep score and highest score
def compare(indices):
    current = display(indices)
    a_followers = data[indices[0]]["follower_count"]
    b_followers = data[indices[1]]["follower_count"]
    if a_followers > b_followers:
        correct = "a"
    else:
        correct = "b"
    
    new_indices = fetch(indices)

    if correct == current:
        return 1, False, new_indices
    else:
        return 0, True, new_indices

## when is game over
def game():
    game_over = False
    score = 0
    index = random.sample(range(len(data)),2)
    while not game_over:
        point, game_over, new_indices = compare(index)
        score += point
        index = new_indices
        if game_over:
            print(f"\nSorry, that's wrong. Final score: {score}\n")
        else:
            print(f"\nYou're right! Current score: {score}\n")
    return score
    
## Ask if they want to play again
new_game = True
while new_game:
    print(f"Highest score is: {highest_score}")
    score = game()    
    try_again = input("Do you want to play again? Type 'yes' or 'no'. ")[0].lower()
    if try_again == "y":
        new_game = True
    else:
        new_game = False

    cls()
    if score > highest_score:
        highest_score = score

