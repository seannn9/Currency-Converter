from tkinter import *
from main import main_func

button_font = ("Helvetica, 40")

def destroy_all():
    for widget in window.winfo_children():
        widget.destroy()

def convert_from(f):
    button.configure(command=lambda t="USD": convert_to(t))
    button1.configure(command=lambda t="PHP": convert_to(t))
    button2.configure(command=lambda t="EUR": convert_to(t))
    return f
    
def convert_to(t):
    destroy_all()
    enter_amount = Entry(window)
    enter_amount.pack()
    submit = Button(window, text="Convert", font=button_font, command=lambda: convert(enter_amount.get()))
    submit.pack()
    return t

def convert(a):
    print(a)
    main_func(convert_from, convert_to, a)

window = Tk()
window.title("Currency Convert")
window.geometry("500x500")
window.resizable(False, False)

button = Button(window, text="USD", font=button_font, width=40, command=lambda f="USD": convert_from(f))
button.pack(side=TOP)

button1 = Button(window, text="PHP", font=button_font, width=40, command=lambda f="PHP": convert_from(f))
button1.pack(side=TOP)

button2 = Button(window, text="EUR", font=button_font, width=40, command=lambda f="EUR": convert_from(f))
button2.pack(side=TOP)

window.mainloop()