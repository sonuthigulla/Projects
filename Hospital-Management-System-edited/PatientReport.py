# This is a sample Report Program. It fetches data from my user_details table to display
from tkinter import ttk
import tkinter as tk
import sqlite3
import datetime as dt


def connect():

    conn = sqlite3.connect("HospitalDB.db")
    print("DATABASE CONNECTION SUCCESSFUL")

    cur = conn.cursor()


def View():

    my_tag = 'normal'
    conn = sqlite3.connect("HospitalDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM PATIENT")
    print("Reterived SUCCESSFUL")
    rows = cur.fetchall()
    for row in rows:
        if my_tag == 'normal':
            my_tag = 'gray'
        else:
            my_tag = 'normal'
        #print(row)

        tree.insert("", tk.END, values=row, tags=my_tag)

    conn.close()

def Exit():  # Exits the program
    root.destroy()



# connect to the database

connect()

root = tk.Tk()
root.resizable(width=2,height=2)
root.option_add('*Font', '18', )
#root.option_add('Calibri', '20')
root.title()

frame = tk.Frame(root)
frame.pack()

#root.geometry('1000x600')

patient_info_frame = tk.LabelFrame(frame, text="", background='')
patient_info_frame.grid(row=0, column=0, sticky="news", padx=0, pady=0)

report_label = tk.Label(patient_info_frame, text="Report on the patients in the System", font='Calibri, 15', anchor="c")
report_label.grid(row=0, column=0)
date = dt.datetime.now()


date_label = tk.Label(patient_info_frame, text=f"{date:%A, %B %d, %Y}", font="Calibri, 12", anchor='e')
date_label.grid(row=1, column=0)  # r=1, column = 0


report_frame = tk.LabelFrame(frame, text="", background='')
report_frame.grid(row=1, column=0, sticky="news", padx=0, pady=0)

#Add a Vertical Scrollbar



s = ttk.Style()
s.theme_use('clam')
font1 = ['Times', 10, 'normal']
# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="lightgray", font=font1)

# Add a Treeview widget
#tree= ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)



tree = ttk.Treeview(report_frame,column=("1", "2", "3", "4", "5", "6", "7", "8"), show='headings')


tree.tag_configure('gray', background='lightgray')
tree.tag_configure('normal', background='white')

tree.column("#1", width=100, anchor=tk.CENTER)
tree.heading("#1", text="PATIENT_ID")
tree.column("#2", width=100, anchor=tk.CENTER)
tree.heading("#2", text=" NAME")
tree.column("#3", width=100, anchor=tk.CENTER)
tree.heading("#3", text="SEX")
tree.column("#4", width=100, anchor=tk.CENTER)
tree.heading("#4", text="BLOOD_GROUP")
tree.column("#5", width=100, anchor=tk.CENTER)
tree.heading("#5", text=" DOB")
tree.column("#6", width=100, anchor=tk.CENTER)
tree.heading("#6", text="ADDRESS")
tree.column("#7", width=100,anchor=tk.CENTER)
tree.heading("#7",  text="CONSULT_TEAM")
tree.column("#8", width=100,anchor=tk.CENTER)
tree.heading("#8", text=" EMAIL")

#tree.grid(row=3, column=0)
tree.pack()

button_frame = tk.LabelFrame(frame, text="", background='')
button_frame.grid(row=2, column=0, sticky="news", padx=10, pady=10)

btnDisplay = tk.Button(button_frame, text="Display", width=10, command=View)
btnExit = tk.Button(button_frame, text="Exit", width=10, command=Exit)

btnDisplay.grid(row=0, column=0, pady=10)
btnExit.grid(row=0, column=1,pady=10)

for widget in button_frame.winfo_children():
    widget.grid_configure(padx=0, pady=0)

root.mainloop()
