import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetics():
    word = input("Enter a word: ")
    try:
        new_list = [nato_dict[i] for i in word.upper()]
    except KeyError:
        print(f"Sorry, {word} isn't a valid word")
        phonetics()
    else:
        print(new_list)


phonetics()
