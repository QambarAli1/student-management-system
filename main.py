import tkinter as tk
from tkinter import ttk
from tkinter.constants import GROOVE
from tkinter.font import BOLD

win = tk.Tk()
win.geometry("1200x600")
win.title("Student Mangement SYstem")

# for title

title_label = tk.Label(win,text="Student Management System",font=("Ariel",25,BOLD),border=12,relief=tk.GROOVE,foreground="yellow",bg="blue")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame()

win.mainloop()