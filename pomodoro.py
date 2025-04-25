import time
from tkinter import *


def start_countdown():
    try:
        total_seconds = int(minutes.get())* 60
        minutes.config(state=DISABLED)
        start.config(state=DISABLED)
        countdown(total_seconds)
    except ValueError:
        timer.config(text="Enter a valid number!")

def countdown(seconds_left):
    mins, secs = divmod(seconds_left, 60)
    timer.config(text=f"{mins:02}:{secs:02}")
    if seconds_left > 0:
        timer_id=Window.after(1000, countdown, seconds_left - 1)
    else:
        timer.config(text="Time's up! ")
        minutes.config(state=NORMAL)
        start.config(state=NORMAL)
def reset_countdown():
    global timer_id
    if timer_id:
        Window.after_cancel(timer_id)
    timer.config(text="00:00")
    minutes.delete(0,END)
    minutes.config(state=NORMAL)
    start.config(state=NORMAL)
    

Window= Tk()
Window.geometry("400x400")
Window.title("Pomodoro Rachid")

icon = PhotoImage(file='Pomodoro.png')
Window.iconphoto(True,icon)

subtitle = Label(Window, text="This is a pomodoro app!",font=("Arial",20,"bold"), fg="white",background='#e6461e')
subtitle.pack()

Window.config(background='#e6461e')
minutes = Entry()
start = Button(Window,text="Start timer",command=start_countdown)
start.config(bg="#3b42bf")
timer=Label(Window,text="00:00", font=("Arial", 40, "bold"),
                    fg="white", bg="#e6461e")

buttons_frame = Frame(Window, bg='#e6461e')
buttons_frame.pack(pady=20)


minutes.pack()
timer.pack()

start.pack(side=LEFT)
reset= Button(Window,text="reset timer",command=reset_countdown)
reset.pack(side=LEFT)
Window.mainloop()
