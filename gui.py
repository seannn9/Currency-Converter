from tkinter import *
from main import main_func

button_font = ("Helveticam, 40")

def convert_from(from_curr):
    window.title("Currency Convert TO")
    if from_curr == "USD":
        return "USD"
    elif from_curr == "EUR":
        return "EUR"
    
def convert_to(convert_from):
    pass

window = Tk()
window.title("Currency Convert FROM")
window.geometry("500x500")
window.resizable(False, False)

button = Button(window, text="USD", font=button_font, width=40, command=convert_from("USD"))
button.pack(side=TOP)

button1 = Button(window, text="PHP", font=button_font, width=40, command=convert_from("PHP"))
button1.pack(side=TOP)

button2 = Button(window, text="EUR", font=button_font, width=40, command=convert_from("EUR"))
button2.pack(side=TOP)

window.mainloop()