from tkinter import*
from tkinter import ttk
import sqlite3
a=Tk()
a.geometry("700x700")
a.title("Student registration from")

def add():
    Name=entry_1.get()
    Email=entry_2.get()
    Age=entry_3.get()
    Gender=combobox.get()
    DOB=entry_5.get()
    Address=entry_6.get()
    Country=combobox.get()
    Course=combobox.get()
    cursor.execute("INSERT INTO student VALUES(?,?,?,?,?,?,?,?)",[Name,Email,Age,Gender,DOB,Address,Country,Course])
    conn.commit()

conn=sqlite3.connect('form.db')
cursor=conn.cursor()
cursor.execute("create table if not exists Student(Name TEXT,Email TEXT,Age INT,Gender TEXT,DOB INT,Address TEXT,Country TEXT,Course TEXT)")

label_0=Label(a,text="Registration form",width=25,font=("Bold",16),bg="Orange").pack(pady=55)
##label.place(x=100,y=100)

label_1=Label(a,text="Name",width=20,font=("Bold",10))
label_1.place(x=80,y=150)
entry_1=Entry(a)
entry_1.place(x=200,y=150)

label_2=Label(a,text="Email",width=20,font=("Bold",10))
label_2.place(x=80,y=200)
entry_2=Entry(a)
entry_2.place(x=200,y=200)

label_3=Label(a,text="Age",width=20,font=("Bold",10))
label_3.place(x=80,y=250)
entry_3=Entry(a)
entry_3.place(x=200,y=250)

label_4=Label(a,text="Gender",width=20,font=("Bold",10))
label_4.place(x=80,y=300)
combobox=ttk.Combobox(a,textvariable="Gender")
combobox["values"]=["male","Female"]
combobox.current(0)
combobox.place(x=200,y=300)

label_5=Label(a,text="DOB",width=20,font=("Bold",10))
label_5.place(x=80,y=350)
entry_5=Entry(a)
entry_5.place(x=200,y=350)

label_6=Label(a,text="Address",width=20,font=("Bold",10))
label_6.place(x=80,y=400)
entry_6=Entry(a)
entry_6.place(x=200,y=400)

label_7=Label(a,text="Country",width=20,font=("Bold",10))
label_7.place(x=80,y=450)
combobox=ttk.Combobox(a,textvariable="Country")
combobox["values"]=["India","Malaysia","Singapore","Australia"]
combobox.current(0)
combobox.place(x=200,y=450)

label_8=Label(a,text="Course",width=20,font=("Bold",10))
label_8.place(x=80,y=500)
combobox=ttk.Combobox(a,textvariable="course")
combobox["values"]=["BBA","Bcom","BCA","MCA","MBA"]
combobox.current(0)
combobox.place(x=200,y=500)

Button(a,text="Submit",width=10,bg="orange",fg="white",command=add).place(x=100,y=550)

Button(a,text="cancel",width=10,bg="orange",fg="white",command=add).place(x=200,y=550)

a.mainloop()













































