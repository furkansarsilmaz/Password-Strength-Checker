import re
from tkinter import messagebox
class Check :
    def __init__(self,saver,increaser):
        self.saver = saver
        self.Increase = increaser

    def Check_Password(self,text):
        """
        Validates the entered password against three regex patterns 
        (strong, medium, weak). 
        Displays messages based on strength and updates the progress bar.
        """
        Password_Regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
        Weak_Regex = r'^(?=.*[a-z])(?=.*[A-Z])[A-Za-z]{6,}'
        Middle_Regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        self.text = text
        Password = self.text.get()

        if re.match(Password_Regex, Password):
            messagebox.showinfo("Succeed", "Password is strong")
            self.saver.Save_Password(Password)  
            self.Increase.increase(99)

        elif re.match(Weak_Regex, Password):
            messagebox.showwarning("Weak", "Password is weak, try again")
            self.Increase.increase(33)

        elif re.match(Middle_Regex, Password):
            messagebox.showwarning("Middle", "Password is mid-level, try again")
            self.Increase.increase(66)
