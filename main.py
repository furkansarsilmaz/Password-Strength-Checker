from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from increase import Increase
from saver import Saver
from checker import Check
import re
import os

class Checker():
    def __init__(self, root):
        """
        Initializes the UI components using Tkinter, 
        setting up labels, entry fields, buttons, and a progress bar.
        """
        self.root = root
        self.root.geometry("300x200")
        self.root.title("Checker")


        self.Menu_Label = Label(self.root, text="Enter a Password", font=("Arial", 14, "bold italic")).pack(pady=10)

        self.Password_Text = Entry(self.root, show="*")
        self.Password_Text.pack()

        self.Progress_Bar = ttk.Progressbar(self.root, mode="determinate")
        self.Progress_Bar.pack(pady=10)

        self.Button_Frame = Frame(self.root, relief=RAISED)
        self.Button_Frame.pack()

        self.saver = Saver()
        self.Increase = Increase(self.Progress_Bar)
        self.check = Check(self.saver,self.Increase)
        
        self.Enter_Button = Button(self.Button_Frame, text="Enter", width=5, height=2, command= lambda: self.check.Check_Password(self.Password_Text))
        self.Enter_Button.pack(pady=10, side=LEFT)

        self.Quit_Button = Button(self.Button_Frame, text="Quit", width=5, height=2, command=self.root.quit)
        self.Quit_Button.pack(side=RIGHT)

if __name__ == "__main__":
    root = Tk()
    Checker(root)
    root.mainloop()