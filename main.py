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

# for details frame 

detail_frame = tk.LabelFrame(win,text="Enter Details",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
detail_frame.place(x=20,y=80,width=420,height=500)

# for data frame 

data_frame = tk.LabelFrame(win,text="Data",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
data_frame.place(x=500,y=80,width=700,height=500)

# for input fields 

rollno_label = tk.Label(detail_frame,text="Roll No",font=("Arial",10))
rollno_label.grid(row=0,column=0,padx=2,pady=2)
rollno_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10))
rollno_entry.grid(row=0,column=1,padx=2,pady=2)

name_label = tk.Label(detail_frame,text="Name",font=("Arial",10))
name_label.grid(row=1,column=0,padx=2,pady=2)
name_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10))
name_entry.grid(row=1,column=1,padx=2,pady=2)

fathername_label = tk.Label(detail_frame,text="Father Name",font=("Arial",10))
fathername_label.grid(row=2,column=0,padx=2,pady=2)
fathername_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10))
fathername_entry.grid(row=2,column=1,padx=2,pady=2)

semester_label = tk.Label(detail_frame,text="Semester",font=("Arial",10))
semester_label.grid(row=3,column=0,padx=2,pady=2)
semester_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10))
semester_entry.grid(row=3,column=1,padx=2,pady=2)

sec_label = tk.Label(detail_frame,text="Section",font=("Arial",10))
sec_label.grid(row=4,column=0,padx=2,pady=2)
sec_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10))
sec_entry.grid(row=4,column=1,padx=2,pady=2)

win.mainloop()