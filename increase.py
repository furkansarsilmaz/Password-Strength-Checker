from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import os

class Increase :
    def __init__(self,Progress_Bar):
        self.progress_bar = Progress_Bar
        
    def increase(self,Ratio):
        """
        Updates the progress bar based on the strength of the password.
        """
        self.progress_bar["value"] = Ratio   