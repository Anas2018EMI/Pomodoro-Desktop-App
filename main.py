from cgitb import text
from re import L
from tabnanny import check
from tkinter import *
from turtle import st

from click import command
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps=0
checked=""
timer_mechanism= None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, checked
    window.after_cancel(timer_mechanism)
    reps=0
    checked=""
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    checkmark_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, checked
    reps+=1
    work_sec= WORK_MIN*5
    short_break_sec= SHORT_BREAK_MIN*5
    long_break_sec = LONG_BREAK_MIN*5
    
    if reps%2==1:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        if reps>1:
            checked+='✔'
            checkmark_label.config(text=checked)
    elif reps%8==0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer_mechanism
    count_min= count//60
    count_sec= count%60
    
    if count_sec < 10:
        count_sec= "0"+ str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        timer_mechanism=window.after(1000, countdown, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Technic")
window.config(padx=100, pady=50, bg=YELLOW)

canvas=Canvas(width=256, height=256,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file='tomato1.png')
canvas.create_image(128,128,image=tomato_img)
timer_text= canvas.create_text(128,160,text="00:00",fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label=Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button=Button(text="Start", bg='white', highlightthickness=0, command=start_timer)
# start_button.bind('<Button-1>',start_timer)
start_button.grid(column=0, row=2)


reset_button=Button(text='Reset', bg='white', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label=Label(font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

















window.mainloop()