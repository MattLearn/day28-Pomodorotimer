import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
COUNTER_ID = ""


# ToDo create a countdown
def countdown(count):
    global REPS
    global COUNTER_ID
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        COUNTER_ID = window.after(1000, countdown, count-1)
    else:
        REPS += 1
        timer_start()


def timer_start():
    global REPS, COUNTER_ID
    phase_check()
    if REPS % 8 == 0:
        header_lbl.config(text="Done!", fg=RED)
        countdown(5)
#        countdown(LONG_BREAK_MIN * 60)
        window.after_cancel(COUNTER_ID)
    elif REPS % 2 == 0:
        header_lbl.config(text="Break", fg=PINK)
        countdown(3)
#        countdown(SHORT_BREAK_MIN)
    else:
        header_lbl.config(text="Work!", fg=GREEN)
        countdown(9)
#        countdown(WORK_MIN* 60)


def reset():
    global REPS, COUNTER_ID
    REPS = 1
    phase_check()
    window.after_cancel(COUNTER_ID)
    header_lbl.config(text="POMODORO", foreground=GREEN)
    canvas.itemconfig(time_txt, text=f"00:00")


def phase_check():
    rep1_checkbox.config(onvalue=1)
    rep2_checkbox.config(onvalue=1)
    rep3_checkbox.config(onvalue=1)
    rep4_checkbox.config(onvalue=1)
    if REPS >= 2:
        rep1_checkbox.config(onvalue=0)
    if REPS >= 4:
        rep2_checkbox.config(onvalue=0)
    if REPS >= 6:
        rep3_checkbox.config(onvalue=0)
    if REPS >= 8:
        rep4_checkbox.config(onvalue=0)


# ToDo create a new window and name it "Pomodoro"
window = Tk()
window.title("Pomodoro")
window.config(width=300, height=300, padx=100, pady=50, bg=YELLOW)

# ToDo create GUI
header_lbl = Label(text="POMODORO", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 40))
header_lbl.grid(column=1, row=0)

start_btn = Button(text="Start", command=timer_start)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

checkbox_canvas = Canvas(width=40, height=40)
rep1_checkbox = Checkbutton(checkbox_canvas, background=YELLOW, state=DISABLED)
rep2_checkbox = Checkbutton(checkbox_canvas, background=YELLOW, state=DISABLED)
rep3_checkbox = Checkbutton(checkbox_canvas, background=YELLOW, state=DISABLED)
rep4_checkbox = Checkbutton(checkbox_canvas, background=YELLOW, state=DISABLED)
rep1_checkbox.grid(column=0, row=0)
rep2_checkbox.grid(column=2, row=0)
rep3_checkbox.grid(column=0, row=1)
rep4_checkbox.grid(column=2, row=1)
checkbox_canvas.grid(column=1, row=3)

reps_lbl = Label(text="Completed Reps", background=YELLOW)
reps_lbl.grid(column=1, row=4)

window.mainloop()
