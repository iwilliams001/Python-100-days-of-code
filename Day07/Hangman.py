import random
from Hangman_art import stages, logo
from Hangman_words import word_list

print(logo)
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)


display = []
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
length = len(chosen_word)
for x in range(length):
    display.append("_")
print(display)


#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

#Create a variable called 'lives' to keep track of the number of lives left. 
lives = 6
guesses = ""

while not end_of_game:
    guess = input("Guess a letter.\n").lower()
    positions = []
    for x in range(length):
        letter = chosen_word[x]
        if letter == guess:
            display[x] = guess
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    if guess not in chosen_word and guess not in guesses:
        lives -= 1
        print(f"You guessed {guess}. That is not in the word so you lose a live.")
    else:
        if guess in guesses:
            print(f"You already guessed {guess}. Try a different letter.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

    if "_" in display and lives > 0:
        end_of_game = False
    else:
        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
        else:
            #If lives goes down to 0 then the game should stop and it should print "You lose."
            end_of_game = True
            print("You lose.")
            print(f'Pssst, the solution is {chosen_word}.')
    
    guesses += guess    