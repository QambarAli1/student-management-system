import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import pyrebase
from tkinter import messagebox

win = tk.Tk()
win.geometry("1340x700")
win.title("Student Mangement System by Qambar Ali and Aman Khan")

config = {
  "apiKey": "AIzaSyB0nCDu482FaIn5Gz4qblrtB7uVlqBIiD8",
  "authDomain": "sudo-app-react.firebaseapp.com",
  "databaseURL": "https://sudo-app-react-default-rtdb.firebaseio.com",
  "projectId": "sudo-app-react",
  "storageBucket": "sudo-app-react.appspot.com",
  "messagingSenderId": "155355720448",
  "appId": "1:155355720448:web:44dd50f736a6401d18e1e5"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

allKeys = db.child("students").get().val()
print(allKeys)

#function adding new students

def addStd():
  Entries=[rollno_entry.get(),name_entry.get(),fathername_entry.get(),gender_entry.get(),email_entry.get(),department_entry.get(),semester_entry.get(),sec_entry.get()]
  biodata = {"rollno" : rollno_entry.get(),
             "name" : name_entry.get(),
             "fathername" : fathername_entry.get(),
             "gender" : gender_entry.get(),
             "email" : email_entry.get(),
             "department" : department_entry.get(),
             "semester" : semester_entry.get(),
             "sec" : sec_entry.get() }

  flag = True
  uniqueRollno = True
  for x in Entries:
      if len(x) == 0:
          flag = False
  allKeys = db.child("students").get().val()
  if allKeys!=None:
      for keys in allKeys:
          if db.child("students").child(keys).get().val()['rollno'] == rollno_entry.get():
              uniqueRollno = False
  if flag == False:
      messagebox.showwarning("warning", "Fill Entries")
      print('Fill Entries')
  if allKeys==None and flag==True:
      print(Entries)
      db.child('students').push(biodata)
      clearEntries()
      clearTreeview()
      allStd()
      messagebox.showinfo("Added", "Student Added Successfully !")
  if uniqueRollno==False:
      messagebox.showinfo("Duplicated", "Roll No Must be Unique !")
  if allKeys != None and uniqueRollno==True:
      print(Entries)
      db.child('students').push(biodata)
      clearEntries()
      clearTreeview()
      allStd()
      messagebox.showinfo("Added", "Student Added Successfully !")


def clearEntries():
    rollno_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    gender_entry.delete(0, 'end')
    fathername_entry.delete(0, 'end')
    gender_entry.set('')
    email_entry.delete(0, 'end')
    department_entry.delete(0, 'end')
    semester_entry.delete(0, 'end')
    sec_entry.delete(0, 'end')


# for title

title_label = tk.Label(win,text="Student Management System",font=("Ariel",25,BOLD),border=12,relief=tk.GROOVE,foreground="yellow",bg="blue")
title_label.pack(side=tk.TOP,fill=tk.X)

# for details frame

detail_frame = tk.LabelFrame(win,text="Details",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
detail_frame.place(x=20,y=80,width=420,height=550)

# for data frame

data_frame = tk.LabelFrame(win,text="Data",font=("Arial",20,BOLD),bd=12,relief=tk.GROOVE)
data_frame.place(x=470,y=80,width=850,height=550)

#*****Inp Variables *****

rollno = tk.StringVar()
name = tk.StringVar()
fathername = tk.StringVar()
gender = tk.StringVar()
email = tk.StringVar()
department= tk.StringVar()
semester = tk.StringVar()
section = tk.StringVar()
search = tk.StringVar()
note = tk.StringVar()


# for input fields

rollno_label = tk.Label(detail_frame,text="Roll No",font=("Arial",10),width=13)
rollno_label.grid(row=0,column=0,padx=10,pady=8)
rollno_entry = tk.Entry(detail_frame , bd=7,font=("Arial",10) , width=28 ,textvariable=rollno)
rollno_entry.grid(row=0,column=1,padx=10,pady=8)

name_label = tk.Label(detail_frame,text="Name",font=("Arial",10),width=13)
name_label.grid(row=1,column=0,padx=10,pady=8)
name_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28 ,textvariable=name)
name_entry.grid(row=1,column=1,padx=10,pady=8)

fathername_label = tk.Label(detail_frame,text="Father Name",font=("Arial",10),width=13)
fathername_label.grid(row=2,column=0,padx=10,pady=8)
fathername_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28,  textvariable=fathername)
fathername_entry.grid(row=2,column=1,padx=10,pady=8)

gender_label = tk.Label(detail_frame,text="Gender",font=("Arial",10),width=13)
gender_label.grid(row=3,column=0,padx=10,pady=8)
gender_entry = ttk.Combobox(detail_frame,font=("Arial",10),width=28,state="readonly",textvariable=gender)
gender_entry['values'] = ("Male", "Female")
gender_entry.grid(row=3,column=1,padx=10,pady=8)

email_label = tk.Label(detail_frame,text="Email",font=("Arial",10),width=13)
email_label.grid(row=4,column=0,padx=10,pady=8)
email_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28 , textvariable=email)
email_entry.grid(row=4,column=1,padx=10,pady=8)

department_label = tk.Label(detail_frame,text="Department",font=("Arial",10),width=13)
department_label.grid(row=5,column=0,padx=10,pady=8)
department_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28 ,textvariable=department)
department_entry.grid(row=5,column=1,padx=10,pady=8)

semester_label = tk.Label(detail_frame,text="Semester",font=("Arial",10),width=13)
semester_label.grid(row=6,column=0,padx=10,pady=8)
semester_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28 ,textvariable=semester)
semester_entry.grid(row=6,column=1,padx=10,pady=8)

sec_label = tk.Label(detail_frame,text="Section",font=("Arial",10),width=13)
sec_label.grid(row=7,column=0,padx=10,pady=8)
sec_entry = tk.Entry(detail_frame,bd=7,font=("Arial",10) , width=28 ,textvariable=section)
sec_entry.grid(row=7,column=1,padx=10,pady=8)


#update record

def updateStd():
    updateRollno = rollno_entry.get()
    allKeys = db.child("students").get().val()
    for keys in allKeys:
        print(keys)
        if db.child("students").child(keys).get().val()['rollno']==updateRollno:
            db.child("students").child(keys).update({'name':name_entry.get()})
            db.child("students").child(keys).update({'fathername':fathername_entry.get()})
            db.child("students").child(keys).update({'email':email_entry.get()})
            db.child("students").child(keys).update({'gender':gender_entry.get()})
            db.child("students").child(keys).update({'department':department_entry.get()})
            db.child("students").child(keys).update({'semester':semester_entry.get()})
            db.child("students").child(keys).update({'sec':sec_entry.get()})
            messagebox.showinfo("Updated", "Updated Successfully !")
    clearEntries()
    clearTreeview()
    allStd()

#delete record

def deleteStd():
    deleteRollno = rollno_entry.get()
    allKeys = db.child("students").get().val()
    for keys in allKeys:
        print(keys)
        if db.child("students").child(keys).get().val()['rollno']==deleteRollno:
            db.child("students").child(keys).remove()
            messagebox.showinfo("Deleted", "Deleted Successfully !")
    clearEntries()
    clearTreeview()
    allStd()


# for button frame

btn_frame = tk.Frame(detail_frame,relief=tk.GROOVE)
btn_frame.place(x=15,y=420,width=350,height=50)

add_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Add",bd=5,font=("Arial",10),width=8, command=addStd)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Update",bd=5,font=("Arial",10),width=8,command=updateStd)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Delete",bd=5,font=("Arial",10),width=8,command=deleteStd)
delete_btn.grid(row=0,column=2,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="lightgrey" ,text="Clear",bd=5,font=("Arial",10),width=8,command=clearEntries)
clear_btn.grid(row=0,column=3,padx=2,pady=2)

#  for search frame
search_frame = tk.Frame(data_frame,bd=6,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_label = tk.Label(search_frame,text="Search by Roll No",font=("Arial",12,BOLD),width=30)
search_label.grid(row=0,column=0,padx=5,pady=5)


search_entry = tk.Entry(search_frame,bd=2,font=("Arial",10) , width=28)
search_entry.grid(row=0,column=1,padx=1,pady=1)


#clear students table

def clearTreeview():
    x = student_data.get_children()
    for items in x:
        student_data.delete(items)

#search for student with roll no

def searchStd():
    allkeys = db.child("students").get().val()
    searchrollno = search_entry.get()
    flag = False
    if allkeys!=None:
        for key in allkeys:
            # print('keys', key)
            # rollnoInsert = db.child("students").child(key).get().val()["rollno"]
            stdrollno = db.child("students").child(key).get().val()["rollno"]
            if searchrollno == db.child("students").child(key).get().val()["rollno"]:
                # student_data.insert('','end',value='')
                flag = True
                clearTreeview()
                # print('found at ',key)
                # print('Record Found')
                rollno.set(db.child("students").child(key).get().val()["rollno"])
                name.set(db.child("students").child(key).get().val()["name"])
                fathername.set(db.child("students").child(key).get().val()["fathername"])
                email.set(db.child("students").child(key).get().val()["email"])
                gender.set(db.child("students").child(key).get().val()["gender"])
                department.set(db.child("students").child(key).get().val()["department"])
                semester.set(db.child("students").child(key).get().val()["semester"])
                section.set(db.child("students").child(key).get().val()["sec"])
                student_data.insert('', 'end', value=(
                    db.child("students").child(key).get().val()["rollno"],
                    db.child("students").child(key).get().val()["name"],
                    db.child("students").child(key).get().val()["fathername"],
                    db.child("students").child(key).get().val()["gender"],
                    db.child("students").child(key).get().val()["email"],
                    db.child("students").child(key).get().val()["department"],
                    db.child("students").child(key).get().val()["semester"],
                    db.child("students").child(key).get().val()["sec"]
                ))
    if flag==True:
        print('Found')
    if flag == False:
        print('Not found')
        messagebox.showinfo("404", "No record found !")


search_btn = tk.Button(search_frame,text="Search", bd = 5, font=("Arial",12,BOLD),width=8,command=searchStd)
search_btn.grid(row=0,column=3,padx=1,pady=1)


# for data view frame to show all students in table


data_view = tk.Frame(data_frame,bg="lightgray",bd=10 , relief=tk.GROOVE)
data_view.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(data_view,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(data_view,orient=tk.HORIZONTAL)

student_data = ttk.Treeview(data_view,columns=("Roll No","Name","Father Name","Gender","Email","Department","Semester","Section") , yscrollcommand=y_scroll.set , xscrollcommand=x_scroll.set)
student_data.heading("Roll No",text="Roll No")
student_data.heading("Name",text="Name")
student_data.heading("Father Name",text="Father Name")
student_data.heading("Email",text="Email")
student_data.heading("Gender",text="Gender")
student_data.heading("Department",text="Department")
student_data.heading("Semester",text="Semester")
student_data.heading("Section",text="Section")

student_data.column("Roll No" , width=50)
student_data.column("Name" , width=100)
student_data.column("Father Name" , width=100)
student_data.column("Email" , width=130)
student_data.column("Gender" , width=50)
student_data.column("Department" , width=80)
student_data.column("Semester" , width=50)
student_data.column("Section" , width=50)
student_data["show"] = "headings"


#show all students data

def allStd():
    allkeys = db.child("students").get().val()
    if allkeys!=None:
        student_data.insert('', 'end', value='')
        for key in allkeys:
            print('keys', key)
            rollnoInsert = db.child("students").child(key).get().val()["rollno"]
            nameInsert = db.child("students").child(key).get().val()["name"]
            fathernameInsert = db.child("students").child(key).get().val()["fathername"]
            genderInsert = db.child("students").child(key).get().val()["gender"]
            emailInsert = db.child("students").child(key).get().val()["email"]
            departmentInsert = db.child("students").child(key).get().val()["department"]
            semesterInsert = db.child("students").child(key).get().val()["semester"]
            secInsert = db.child("students").child(key).get().val()["sec"]
            student_data.insert('', 'end', value=(
            rollnoInsert, nameInsert, fathernameInsert, genderInsert, emailInsert, departmentInsert, semesterInsert,
            secInsert))
    else:
        print('No records found')

allStd()
y_scroll.config(command=student_data.yview)
x_scroll.config(command=student_data.xview)
y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_data.pack(fill=tk.BOTH,expand=True)
win.mainloop()