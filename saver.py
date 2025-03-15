from tkinter import messagebox
import os

class Saver :

    def Save_Password(self, Password):
        Password = str(Password)
        Path = os.getcwd()  
        File_Path = os.path.join(Path, "Passwords.txt")  
        with open(File_Path, "w") as file:  
            file.write(Password)
        messagebox.showinfo("Saved", f"Password saved to {File_Path}")