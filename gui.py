from tkinter import *
from main import main_func

button_font = ("Helvetica, 40")

def destroy_all():
    for widget in window.winfo_children():
        widget.destroy()

def create_to():
    # create convert to options 
    button3 = Button(window, text="USD", font=button_font, width=40,command=to_USD)
    button3.pack(side=TOP)
    button4 = Button(window, text="PHP", font=button_font, width=40, command=to_PHP)
    button4.pack(side=TOP)
    button5 = Button(window, text="EUR", font=button_font, width=40, command=to_EUR)
    button5.pack(side=TOP)

def create_submit():
    def get_amount():
        amount.get()
    amount = Entry()
    amount.pack()
    submit = Button(window, text="Submit", font=("Helvetica, 20"), command=get_amount)
    submit.pack()
    money = get_amount()
    return money


def from_USD():
    destroy_all()
    create_to()
    return "USD"
    
def from_PHP():
    destroy_all()
    create_to()
    return "PHP"

def from_EUR():
    destroy_all()
    create_to()
    return "EUR"

# currency to convert to
def to_USD():
    destroy_all()
    create_submit()
    return "USD"

def to_PHP():
    destroy_all()
    return "PHP"

def to_EUR():
    destroy_all()
    return "EUR"


  
window = Tk()
window.title("Currency Convert")
window.geometry("500x500")
window.resizable(False, False)

button = Button(window, text="USD", font=button_font, width=40, command=from_USD)
button.pack(side=TOP)

button1 = Button(window, text="PHP", font=button_font, width=40, command=from_PHP)
button1.pack(side=TOP)

button2 = Button(window, text="EUR", font=button_font, width=40, command=from_EUR)
button2.pack(side=TOP)

window.mainloop()