from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
check = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global check, REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg=GREEN)
    check = ""
    REPS = 0
    label2.config(text=check)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if REPS % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label1.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0 and REPS > 0:
            check += "✓"
            label2.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Labels
label1 = Label()
label1.config(text="Timer", padx=0, pady=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label1.grid(column=1, row=0)

label2 = Label()
label2.config(text="", padx=0, pady=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
label2.grid(column=1, row=3)

# Buttons
# calls action() when pressed
start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
