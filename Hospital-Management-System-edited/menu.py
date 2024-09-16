from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from patient_form1 import Patient
from room_form import Room
from appointment_form import Appointment
from employee_form import Employee
from billing_form import Billing

conn = sqlite3.connect("HospitalDB.db")

print("DATABASE CONNECTION SUCCESSFUL")


# Class For Menu
class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="#FAEBD7")
        self.frame = Frame(self.master, bg="#FAEBD7")
        self.frame.pack()

        self.lblTitle = Label(self.frame, text="MAIN MENU", font="Helvetica 20 bold", bg="#FAEBD7")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # ===========BUTTONS=============
        self.button1 = Button(self.master, text="1.PATIENT REGISTRATION", width=30, font="Calibre 14 bold",
                              bg="#3498db", command=self.Patient_Reg)
        self.button1.pack(pady=10)

        self.button2 = Button(self.master, text="2.ROOM ALLOCATION", width=30, font="Helvetica 14 bold",
                              bg="#3498db", command=self.Room_Allocation)
        self.button2.pack(pady=10)

        self.button3 = Button(self.master, text="3.EMPLOYEE REGISTRATION", width=30, font="Helvetica 14 bold",
                              bg="#3498db", command=self.Employee_Reg)
        self.button3.pack(pady=10)

        self.button4 = Button(self.master, text="4.BOOK APPOINTMENT", width=30, font="Helvetica 14 bold",
                              bg="#3498db", command=self.Appointment_Form)
        self.button4.pack(pady=10)

        self.button5 = Button(self.master, text="5.PATIENT BILL", width=30, font="Helvetica 14 bold",
                              bg="#3498db", command=self.Billing_Form)
        self.button5.pack(pady=10)

        self.button6 = Button(self.master, text="6.EXIT", width=30, font="Helvetica 14 bold", bg="#3498db",
                              command=self.Exit)
        self.button6.pack(pady=10)

    # Function to Exit Menu Window
    def Exit(self):
        self.master.destroy()

    # Function to open Patient Registration Window
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)

    # Function to open Room Allocation Window

    def Room_Allocation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)

    # Function to open Employee Registration Window
    def Employee_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Employee(self.newWindow)

    # Function to open Appointment Window
    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)

    # Function to open Billing Window
    def Billing_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)