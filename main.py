from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#EF6262"
DARK_BLUE = "#1D5B79"
BLUE = "#468B97"
YELLOW = "#F3AA60"
FONT_NAME = "Courier"
BLACK = "#000000"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start_button.config(state=NORMAL)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=BLUE)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=DARK_BLUE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    if 10 > int(count_sec):
        count_sec = f"0{count_sec}"
    if 10 > count_min:
        count_min = f"0{count_min}"

    proper_timer = f"{count_min}:{count_sec}"

    canvas.itemconfig(timer_text, text=proper_timer)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        start_button.config(state=DISABLED)
    if count == 0:
        start_timer()
        check = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            check += "✔"
        check_mark.config(text=check)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, fg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=BLUE, bg=YELLOW)
check_mark.grid(row=3, column=1)

title_label = Label(text="Timer", fg=BLUE, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(row=0, column=1)




window.mainloop()