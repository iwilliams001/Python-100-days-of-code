# Get the names
with open("./Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.read().splitlines()

# Get the draft letter
with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    raw_letter = letter_file.read()

# Create new personalized letters
for name in names:
    new_letter = raw_letter.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
