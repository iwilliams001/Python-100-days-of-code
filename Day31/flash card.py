from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- GET CSV DATA ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict('records')
else:
    data_dict = data.to_dict('records')


# ---------------------------- WRONG BUTTON ACTION ------------------------------- #
def wrong():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_title, text=f"French", fill="black")
    canvas.itemconfig(canvas_word, text=f"{current_card["French"]}", fill="black")
    timer = window.after(3000, flip_back, current_card)


# ---------------------------- RIGHT BUTTON ACTION --------------------------- #
def remove_card():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    wrong()


# ---------------------------- FLIPPING MECHANISM ------------------------------- #
def flip_back(card):
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_title, text=f"English", fill="white")
    canvas.itemconfig(canvas_word, text=f"{card["English"]}", fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 253, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=wrong)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=1)

timer = window.after(3000, flip_back, current_card)
wrong()

window.mainloop()
