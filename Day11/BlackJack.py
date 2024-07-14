import os
cls = lambda: os.system('cls')
#cls()
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
    ''' Deal cards.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    ''' Calculate the score of cards in hand.'''
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)


def user_game():
    ''' Find out if the game has ended and if the user wants to draw more cards.'''
    game_over = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0:
        game_over = True
    while game_over == False:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")[0].lower()
        if hit == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
            game_over = True
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    return user_cards, computer_cards, user_score, computer_score

def computer_game():
    ''' Forces deal to draw more cards if score is below 17.'''
    user_cards, computer_cards, user_score, computer_score = user_game()

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    return user_score, computer_score

def compare():
    ''' Decides the winner of the game.'''
    user_score, computer_score = computer_game()
    if (user_score == computer_score) and (user_score < 21):
        print(f"Your final hand: {user_cards}, your final score: {user_score}")
        print(f"Computer's cards: {computer_cards}, computer's score: {computer_score}")
        print("Draw")
    elif computer_score == 0:
        print(f"Computer hits a Blackjack: {computer_cards}")
        print("Computer wins")
    elif user_score == 0:
        print(f"You hit a Blackjack: {user_cards}")
        print("you win")
    elif user_score > 21:
        print(f"Your final hand: {user_cards}, your final score: {user_score}")
        print("You went over. You lose")
    elif computer_score > 21:
        print(f"Your final hand: {user_cards}, your final score: {user_score}")
        print(f"Computer's cards: {computer_cards}, computer's score: {computer_score}")
        print("You win")
    else:
        print(f"Your final hand: {user_cards}, your final score: {user_score}")
        print(f"Computer's cards: {computer_cards}, computer's score: {computer_score}")
        if user_score > computer_score:
            print("You win")
        else:
            print("Computer wins")

new_game = True
while new_game:
    user_cards = []
    computer_cards = []

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    compare()
    cont = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")[0].lower()
    if cont == "y":
        new_game = True
    else:
        new_game = False
    cls()

