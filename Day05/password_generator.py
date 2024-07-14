# Password Generator Project
import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many characters would you like in your password? It should be at least 4.\n"))

number_upper = random.randint(1, nr_letters - 3)
upper_sample = random.choices(upper_letters, k=number_upper)
number_lower = random.randint(1, nr_letters - number_upper - 2)
lower_sample = random.choices(lower_letters, k=number_lower)
number_num = random.randint(1, nr_letters - number_upper - number_lower - 1)
numb_sample = random.choices(numbers, k=number_num)
number_symb = nr_letters - number_upper - number_lower - number_num
symb_sample = random.choices(symbols, k=number_symb)

items = [upper_sample, lower_sample, numb_sample, symb_sample]
temp = []
password_list = []
for item in items:
    temp.extend(item)

for x in range(1, nr_letters + 1):
    y = random.choice(temp)
    temp.remove(y)
    password_list.append(y)

password = ""
for element in password_list:
    password += element
print(f"I suggest you use\n{password}")
