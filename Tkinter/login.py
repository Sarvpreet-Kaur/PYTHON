from tkinter import *;

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == 'user' and password == 'pass':
        status_label.config(text = "Login Successful", fg = "green")
    else:
        status_label.config(text = "Invalid Credentials", fg = "red")
    
    
root = Tk()
root.title("Login Form")
root.geometry("300x300")
root.resizable(False, False)

username_label = Label(root, text="Username")
username_label.grid(row = 0, column = 0, padx = 10, pady = 10)

password_label = Label(root, text="Password")
password_label.grid(row = 1, column = 0, padx = 10, pady = 10)

status_label = Label(root, text="")
status_label.grid(row = 3, column = 0, padx = 10, pady = 10)

username_entry = Entry(root)
username_entry.grid(row = 0, column=1, padx=10, pady=10)

password_entry = Entry(root)
password_entry.grid(row = 1, column=1, padx=10, pady=10)

login_button = Button(root, text = "Login", command = login)
login_button.grid(row = 2, column = 0, columnspan=2, pady=10)

root.mainloop()