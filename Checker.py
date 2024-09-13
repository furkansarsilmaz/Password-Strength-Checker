from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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

        self.Enter_Button = Button(self.Button_Frame, text="Enter", width=5, height=2, command=self.Check_Password)
        self.Enter_Button.pack(pady=10, side=LEFT)

        self.Quit_Button = Button(self.Button_Frame, text="Quit", width=5, height=2, command=self.root.quit)
        self.Quit_Button.pack(side=RIGHT)

    def Check_Password(self):
        """
        Validates the entered password against three regex patterns 
        (strong, medium, weak). 
        Displays messages based on strength and updates the progress bar.
        """
        Password_Regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
        Weak_Regex = r'^(?=.*[a-z])(?=.*[A-Z])[A-Za-z]{6,}'
        Middle_Regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        Password = self.Password_Text.get()

        if re.match(Password_Regex, Password):
            messagebox.showinfo("Succeed", "Password is strong")
            self.Save_Password(Password)  
            self.Increase(99)

        elif re.match(Weak_Regex, Password):
            messagebox.showwarning("Weak", "Password is weak, try again")
            self.Increase(33)

        elif re.match(Middle_Regex, Password):
            messagebox.showwarning("Middle", "Password is mid-level, try again")
            self.Increase(66)

    def Save_Password(self, Password):
        """
        Saves the valid password into a file named Passwords.txt in the current directory.
        """
        Password = str(Password)
        Path = os.getcwd()  
        File_Path = os.path.join(Path, "Passwords.txt")  
        with open(File_Path, "w") as file:  
            file.write(Password)

        messagebox.showinfo("Saved", f"Password saved to {File_Path}")

    
    def Increase(self,Ratio):
        """
        Updates the progress bar based on the strength of the password.
        """
        self.Progress_Bar.step(Ratio)

if __name__ == "__main__":
    root = Tk()
    Checker(root)
    root.mainloop()
