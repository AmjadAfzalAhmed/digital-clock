from tkinter import *
import datetime 


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%H')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_hr.after(200, date_time)


clock = Tk()
clock.title("     Digital Clock")
clock.geometry("1000x400")
clock.config(bg="#43cea2")


lab_hr = Label(clock, text="00", font=("calibri", 45, 'bold'),
            bg="blue", fg="white")
lab_hr.place(x=120, y=45, width=110, height=90)

lab_min = Label(clock, text="00", font=("calibri", 45, 'bold'),
            bg="blue", fg="white")
lab_min.place(x=340, y=45, width=110, height=90)

lab_sec = Label(clock, text="00", font=("calibri", 45, 'bold'),
            bg="blue", fg="white")
lab_sec.place(x=560, y=45, width=110, height=90)

lab_am = Label(clock,text="00", font=("calibri", 45, 'bold'),
            bg="blue", fg="white")
lab_am.place(x=780, y=45, width=110, height=90)

lab_colon1 = Label(clock, text="hour", font=("calibri", 25, 'bold'),
            bg="blue", fg="white")
lab_colon1.place(x=120, y=150, width=110, height=40)

lab_colon2 = Label(clock, text="min", font=("calibri", 25, 'bold'),
            bg="blue", fg="white")
lab_colon2.place(x=340, y=150, width=110, height=40)

lab_colon3 = Label(clock, text="sec", font=("calibri", 25, 'bold'),
            bg="blue", fg="white")
lab_colon3.place(x=560, y=150, width=110, height=40)

lab_colon4 = Label(clock, text="AM/PM", font=("calibri", 25, 'bold'),
            bg="blue", fg="white")
lab_colon4.place(x=780, y=150, width=110, height=40)


date_time()
clock.mainloop()