from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("200x200")

def show_message():
    messagebox.showinfo("Alert", "A virus has been found on your device.")

button = Button(root, text="Scan for the virus", command=show_message)
button.place(x=40 , y=80)

root.mainloop()