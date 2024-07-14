from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # Determine the number of each type of character
    nr_letters = random.randint(13, 17)
    number_upper = random.randint(1, nr_letters - 3)
    number_lower = random.randint(1, nr_letters - number_upper - 2)
    number_num = random.randint(1, nr_letters - number_upper - number_lower - 1)
    number_symb = nr_letters - number_upper - number_lower - number_num

    # Randomly sample characters from each set
    upper_sample = random.sample(upper_letters, number_upper)
    lower_sample = random.sample(lower_letters, number_lower)
    numb_sample = random.sample(numbers, number_num)
    symb_sample = random.sample(symbols, number_symb)

    # Combine the samples and shuffle to create the password
    password_list = upper_sample + lower_sample + numb_sample + symb_sample
    random.shuffle(password_list)
    random_password = ''.join(password_list)
    password_entry.insert(END, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    # Reading old data
                    data = json.load(file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    # Create new file
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH SETUP --------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message=f"No Data File Found")
    except KeyError:
        messagebox.showinfo(title=f"Error", message=f"No details for the website exists")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

# Text Entry
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.insert(END, string="isaacwilliams1738@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
