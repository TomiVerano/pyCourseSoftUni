import re
import tkinter as tk

def validate_email():
    email = entry_email.get()


root = tk.Tk()
root.geometry("500x500")
root.title('Email validator')


label_instructions = tk.Label()
