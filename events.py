from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")


def handle_keypress(event):
    print(event.char)   


window.bind("<Key>", handle_keypress)
window.mainloop()