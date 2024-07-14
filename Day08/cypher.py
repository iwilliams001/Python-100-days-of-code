alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(text,shift,direction):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            old_position = alphabet.index(letter)
            if direction == "encode":
                new_position = (old_position + shift) % 26
            if direction == "decode":
                new_position = (old_position + 26 - shift) % 26
            new_letter = alphabet[new_position]
        else:
            new_letter = letter
        cipher_text += new_letter
    print(f"The {direction}d text is {cipher_text}")


restart = "y"
while restart == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    restart = input("Do you want to decipher another message? Yes or No?:\n")[0].lower()