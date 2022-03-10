from tkinter import *


def apple_button_click():
    print('click apple')


def banana_button_click():
    print('click banana')


app = Tk()

apple = Button(app, text="Apple", command=apple_button_click())
apple.grid(padx=10, pady=10)

banana = Button(app, text="Banana", command=banana_button_click())
banana.grid(padx=10, pady=10)

app.mainloop()
