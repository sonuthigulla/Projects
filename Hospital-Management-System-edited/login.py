from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

from menu import Menu


def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


# MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self, master):
        # public data mambers
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="#3498db")  # Hex color code for a shade of blue

        # Load the image
        img = Image.open(r"E:\Govind\Hospital-Management-System\hospital_logo.png")
        img = img.resize((300, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        self.frame = Frame(self.master, bg='#FAEBD7')  # Set background color to the same shade of blue
        self.frame.pack(fill=BOTH, expand=True)

        # Add a label to display the image on the left side
        self.img_label = Label(self.frame, image=self.photo,
                               bg='#FAEBD7')  # Set background color to the same shade of blue
        self.img_label.grid(row=0, column=0, rowspan=4, padx=20, pady=20, sticky="nsew")

        self.LoginFrame = Frame(self.frame, bg='#FAEBD7')  # Set background color to the same shade of blue
        self.LoginFrame.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.lblTitle = Label(self.LoginFrame, text="HEALTH HARBOR SYSTEM", font="Roboto 20 bold", bg="#FAEBD7",
                              fg="black")  # Set background color to a light shade
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblUsername = Label(self.LoginFrame, text="Username", font="Verdana 14 bold", bg="#FAEBD7", bd=10)
        self.lblUsername.grid(row=1, column=0, sticky='e')
        self.entryUsername = Entry(self.LoginFrame, font="Verdana 14 bold", textvariable=self.Username, bd=2)
        self.entryUsername.grid(row=1, column=1)

        self.lblPassword = Label(self.LoginFrame, text="Password", font="Verdana 14 bold", bg="#FAEBD7", bd=10)
        self.lblPassword.grid(row=2, column=0, sticky='e')
        self.entryPassword = Entry(self.LoginFrame, font="Verdana 14 bold", show="*", textvariable=self.Password, bd=2)
        self.entryPassword.grid(row=2, column=1)

        self.btnLogin = Button(self.LoginFrame, text="Login", font="Helvetica 10 bold", width=10, bg="green",
                               fg="black", command=self.Login_system)  # Green color for the login button
        self.btnLogin.grid(row=3, column=0, pady=20, sticky='e')
        self.btnExit = Button(self.LoginFrame, text="Exit", font="Helvetica 10 bold", width=10, bg="#e74c3c",
                              fg="black", command=self.Exit)  # Red color for the exit button
        self.btnExit.grid(row=3, column=1, pady=20)

    # public member function
    # Function for LOGIN
    def Login_system(self):

        S1 = (self.Username.get())
        S2 = (self.Password.get())
        if (S1 == 'admin' and S2 == '1234'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        elif (S1 == 'root' and S2 == '4321'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM", "PLEASE ENTER VALID USERNAME AND PASSWORD")

    # Function for Exit
    def Exit(self):
        self.master.destroy()


if __name__ == "__main__":
    main()
