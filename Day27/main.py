from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.config(padx=20, pady=20)


def convert(miles):
    return miles * 1.609344


# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)

# Labels
label1 = Label()
label1.config(text="Miles", padx=20, pady=20)
label1.grid(column=2, row=0)

# Labels
label2 = Label()
label2.config(text="is equal to", padx=20, pady=20)
label2.grid(column=0, row=1)

# Labels
label3 = Label()
label3.config(text=0, padx=20, pady=20)
label3.grid(column=1, row=1)

# Labels
label4 = Label()
label4.config(text="Km", padx=20, pady=20)
label4.grid(column=2, row=1)


# Buttons
def action():
    miles = convert(float(entry.get()))
    label3["text"] = round(miles, 2)


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()
