import pymysql as mysql
from tkinter import *

con = mysql.connect(user="root", password="root", database="Student", host="localhost")
c = con.cursor()


def show1():
    sql_query = "insert into gui_table values(%s,%s)"
    arr = (e1.get(), e2.get())
    c.execute(sql_query, arr)
    con.commit()
    print('Record Submitted...')


def show2():
    sql_query = "update gui_table set name=%s where id= %s"
    arr = (e2.get(), e1.get())
    c.execute(sql_query, arr)
    con.commit()
    print('Record Submitted...')


def show3():
    sql_query = "delete from gui_table where id=%s"
    arr = (e1.get(),)
    c.execute(sql_query, arr)
    con.commit()
    print('Record Submitted...')


def name():
    sql_query = "select name from gui_table where id=%s"
    arr = (e1.get(),)
    c.execute(sql_query, arr)
    name = c.fetchone()[0]
    # set the text of the entry widget to the retrieved name
    e2.delete(0, END)
    e2.insert(0, name)
    con.commit()


root = Tk()
root.geometry("500x500")
root.title("First Root Window....")
f = Frame(root, height=500, width=500, bg="sky blue")
f.pack(fill=BOTH, expand=True)
# Label....
l1 = Label(f, text="Id: ", bg="white", width=10, font=("times new roman", 10, "bold"))
l1.grid(row=0, column=1)

e1 = Entry(f, width=10)
e1.grid(row=0, column=2)

l2 = Label(f, text="Name: ", bg="white", width=10, font=("times new roman", 10, "bold"))
l2.grid(row=1, column=1)

e2 = Entry(f, width=10)
e2.grid(row=1, column=2)

# Buttons....
b1 = Button(f, text="Save", bg="WHITE", font=("arial", 10, "bold"), width=10, command=show1)
b1.grid(row=2, column=1)
b2 = Button(f, text="Update", bg="WHITE", font=("arial", 10, "bold"), width=10, command=show2)
b2.grid(row=2, column=2)
b3 = Button(f, text="Delete", bg="WHITE", font=("arial", 10, "bold"), width=10, command=show3)
b3.grid(row=2, column=3)
b4 = Button(f, text="Select/Show", bg="WHITE", font=("arial", 10, "bold"), width=10, command=name)
b4.grid(row=2, column=4)
b5 = Button(f, text="Clear", bg="WHITE", font=("arial", 10, "bold"), width=10)
b5.grid(row=2, column=5)
root.mainloop()
