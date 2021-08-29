import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import GROOVE
from tkinter.font import BOLD
from typing import Text

win = tk.Tk()
win.geometry("1200x600")
win.title("Student Mangement SYstem")

# for title

title_label = tk.Label(win,text="Student Management System",font=("Ariel",25,BOLD),border=12,relief=tk.GROOVE,foreground="yellow",bg="blue")
title_label.pack(side=tk.TOP,fill=tk.X)

# for details frame 

detail_frame = tk.LabelFrame(win,text="Details",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
detail_frame.place(x=20,y=80,width=420,height=500)

# for data frame 

data_frame = tk.LabelFrame(win,text="Data",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
data_frame.place(x=470,y=80,width=700,height=500)


# for input fields 

rollno_label = tk.Label(detail_frame,text="Roll No",font=("Arial",10),width=13)
rollno_label.grid(row=0,column=0,padx=10,pady=8)
rollno_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
rollno_entry.grid(row=0,column=1,padx=10,pady=8)

name_label = tk.Label(detail_frame,text="Name",font=("Arial",10),width=13)
name_label.grid(row=1,column=0,padx=10,pady=8)
name_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
name_entry.grid(row=1,column=1,padx=10,pady=8)

fathername_label = tk.Label(detail_frame,text="Father Name",font=("Arial",10),width=13)
fathername_label.grid(row=2,column=0,padx=10,pady=8)
fathername_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
fathername_entry.grid(row=2,column=1,padx=10,pady=8)

gender_label = tk.Label(detail_frame,text="Gender",font=("Arial",10),width=13)
gender_label.grid(row=3,column=0,padx=10,pady=8)
gender_entry = ttk.Combobox(detail_frame,font=("Arial",10),width=28,state="readonly")
gender_entry['values'] = ("Male", "Female")
gender_entry.grid(row=3,column=1,padx=10,pady=8)

email_label = tk.Label(detail_frame,text="Email",font=("Arial",10),width=13)
email_label.grid(row=4,column=0,padx=10,pady=8)
email_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
email_entry.grid(row=4,column=1,padx=10,pady=8)

department_label = tk.Label(detail_frame,text="Department",font=("Arial",10),width=13)
department_label.grid(row=5,column=0,padx=10,pady=8)
department_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
department_entry.grid(row=5,column=1,padx=10,pady=8)

semester_label = tk.Label(detail_frame,text="Semester",font=("Arial",10),width=13)
semester_label.grid(row=6,column=0,padx=10,pady=8)
semester_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
semester_entry.grid(row=6,column=1,padx=10,pady=8)

sec_label = tk.Label(detail_frame,text="Section",font=("Arial",10),width=13)
sec_label.grid(row=7,column=0,padx=10,pady=8)
sec_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28)
sec_entry.grid(row=7,column=1,padx=10,pady=8)

# for button frame 

btn_frame = tk.Frame(detail_frame,relief=tk.GROOVE)
btn_frame.place(x=15,y=380,width=350,height=50)

add_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Add",bd=5,font=("Arial",10),width=8)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Update",bd=5,font=("Arial",10),width=8)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Delete",bd=5,font=("Arial",10),width=8)
delete_btn.grid(row=0,column=2,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Clear",bd=5,font=("Arial",10),width=8)
clear_btn.grid(row=0,column=3,padx=2,pady=2)


#  for search frame 
search_frame = tk.Frame(data_frame,bd=6,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X) 

search_label = tk.Label(search_frame,text="Search",font=("Arial",12,BOLD),width=8)
search_label.grid(row=0,column=0,padx=5,pady=5)
search_by = ttk.Combobox(search_frame,font=("Arial",10) , state="readonly")
search_by["values"] = ("Roll No","Name","Father Name","Email")
search_by.grid(row=0,column=1,padx=1,pady=1)
search_btn = tk.Button(search_frame,text="Search", bd = 5, font=("Arial",12,BOLD),width=8)
search_btn.grid(row=0,column=2,padx=1,pady=1)

allData_btn = tk.Button(search_frame,text="All Students" , bd = 5 ,font=("Arial",12,BOLD),width=10)
allData_btn.grid(row=0,column=3,padx=1,pady=1)

# for data view frame 

data_view = tk.Frame(data_frame,bg="lightgray",bd=10 , relief=tk.GROOVE)
data_view.pack(fill=tk.BOTH,expand=True)

win.mainloop()