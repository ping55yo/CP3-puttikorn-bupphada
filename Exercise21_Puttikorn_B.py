from tkinter import *
import math

def leftClick(event):
    result = float(TextW.get()) / math.pow(float(TextH.get())/100,2)
    if result >= 30.0:
        lableR.configure(text = "อ้วนมาก")
    elif result >= 29.9:
        lableR.configure(text = "อ้วน")
    elif result >= 24.9:
        lableR.configure(text = "น้ำหนักเกิน")
    elif result >=  22.9:
        lableR.configure(text = "น้ำหนักปกติ เหมาะสม")
    elif result <= 18.5:
        lableR.configure(text = "ผอมเกินไป")

Window = Tk()
lableH = Label(Window,text = "ส่วนสูง cm")
lableH.grid(row=0,column=0)
TextH = Entry(Window)
TextH.grid(row=0,column=1)
lableW = Label(Window,text = "ส่วนสูง kg")
lableW.grid(row=1,column=0)
TextW = Entry(Window)
TextW.grid(row=1,column=1)
calbutton = Button(Window,text="คำตอบ")
calbutton.grid(row=2,column=0)
calbutton.bind('<Button-1>',leftClick)
lableR = Label(Window,text = "BMI")
lableR.grid(row=2,column=1)
print(type(TextH))
print(type(lableH))
print(type(calbutton))
Window.mainloop()
