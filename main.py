import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import GROOVE
from tkinter.font import BOLD

win = tk.Tk()
win.geometry("1200x600")
win.title("Student Mangement SYstem")

# for title

title_label = tk.Label(win,text="Student Management System",font=("Ariel",25,BOLD),border=12,relief=tk.GROOVE,foreground="yellow",bg="blue")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Enter Details",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
detail_frame.place(x=20,y=80,width=420,height=500)

data_frame = tk.LabelFrame(win,text="Data",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
data_frame.place(x=500,y=80,width=700,height=500)

win.mainloop()