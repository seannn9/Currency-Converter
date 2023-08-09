from tkinter import *
from main import convert

window = Tk()
window.title("Currency Convert")
window.geometry("500x500")
window.resizable(False, False)

from_label = Label(window, text="From", font=("roboto", 20))
from_label.pack(pady=10)

button = Button(window)

window.mainloop()