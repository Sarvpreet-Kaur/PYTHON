from tkinter import *
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light green")
    root.title("Simple Calculator")
    root.geometry("300x300")

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=85, ipady = 10)

    # Number buttons
    btn1 = Button(root, text='1', fg='black', bg='pink', command=lambda: press(1), height=2, width=9)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='pink', command=lambda: press(2), height=2, width=9)
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='black', bg='pink', command=lambda: press(3), height=2, width=9)
    btn3.grid(row=2, column=2)
    btn4 = Button(root, text='4', fg='black', bg='pink', command=lambda: press(4), height=2, width=9)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='black', bg='pink', command=lambda: press(5), height=2, width=9)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='black', bg='pink', command=lambda: press(6), height=2, width=9)
    btn6.grid(row=3, column=2)
    btn7 = Button(root, text='7', fg='black', bg='pink', command=lambda: press(7), height=2, width=9)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='black', bg='pink', command=lambda: press(8), height=2, width=9)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='black', bg='pink', command=lambda: press(9), height=2, width=9)
    btn9.grid(row=4, column=2)
    btn0 = Button(root, text='0', fg='black', bg='pink', command=lambda: press(0), height=2, width=9)
    btn0.grid(row=5, column=0)

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='pink', command=lambda: press('+'), height=2, width=9)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='pink', command=lambda: press('-'), height=2, width=9)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', fg='black', bg='pink', command=lambda: press('*'), height=2, width=9)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', fg='black', bg='pink', command=lambda: press('/'), height=2, width=9)
    div.grid(row=5, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='pink', command=equal, height=2, width=9)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='black', bg='pink', command=clear, height=2, width=9)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='black', bg='pink', command=lambda: press('.'), height=2, width=9)
    dot.grid(row=6, column=0)

    root.mainloop()