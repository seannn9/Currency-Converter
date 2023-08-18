from tkinter import *
from main import main_func

button_font = ("Helvetica, 40")

def from_USD():
    global button
    window.title("Currency Convert TO")
    return "USD"
    
def from_PHP():
    window.title("Currency Convert TO")
    return "PHP"

def from_EUR():
    window.title("Currency Convert TO")
    return "EUR"
    
def convert_to(convert_from):
    pass

window = Tk()
window.title("Currency Convert FROM")
window.geometry("500x500")
window.resizable(False, False)

button = Button(window, text="USD", font=button_font, width=40, command=from_USD)
button.pack(side=TOP)

button1 = Button(window, text="PHP", font=button_font, width=40, command=from_PHP)
button1.pack(side=TOP)

button2 = Button(window, text="EUR", font=button_font, width=40, command=from_EUR)
button2.pack(side=TOP)

window.mainloop()