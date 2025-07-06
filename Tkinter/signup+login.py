from tkinter import *
from tkinter import messagebox
import os

# File to store users
USER_FILE = "Tkinter\\users.txt"

def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as f:
        for line in f:
            if line.strip().split(",")[0] == username:
                return True
    return False

def check_credentials(username, password):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as f:
        for line in f:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                return True
    return False

def signup():
    def register_user():
        user = username_entry.get()
        pwd = password_entry.get()

        if not user or not pwd:
            messagebox.showwarning("Input Error", "All fields required.")
            return

        if user_exists(user):
            messagebox.showerror("Error", "Username already exists.")
        else:
            save_user(user, pwd)
            messagebox.showinfo("Success", "User registered successfully!")
            signup_win.destroy()

    signup_win = Toplevel(root)
    signup_win.title("Sign Up")
    signup_win.geometry("300x200")
    signup_win.configure(bg="lightyellow")

    Label(signup_win, text="Username", bg="lightyellow").pack(pady=(20, 5))
    username_entry = Entry(signup_win)
    username_entry.pack()

    Label(signup_win, text="Password", bg="lightyellow").pack(pady=5)
    password_entry = Entry(signup_win, show="*")
    password_entry.pack()

    Button(signup_win, text="Register", command=register_user, bg="blue", fg="white").pack(pady=15)

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if check_credentials(user, pwd):
        messagebox.showinfo("Login Success", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")

def reset():
    username_entry.delete(0, END)
    password_entry.delete(0, END)

# Main login window
root = Tk()
root.title("Login System")
root.geometry("300x300")
root.configure(bg="black")

Label(root, text="Login Page", font=("Arial", 16), bg="black", fg="white").pack(pady=10)

Label(root, text="Username:", font=("Arial", 12), bg="black", fg="white").pack(pady=(10, 2))
username_entry = Entry(root)
username_entry.pack()

Label(root, text="Password:", font=("Arial", 12), bg="black", fg="white").pack(pady=(10, 2))
password_entry = Entry(root, show="*")
password_entry.pack()

Button(root, text="Login", command=login, bg="green", fg="white", width=15).pack(pady=10)
Button(root, text="Reset", command=reset, bg="gray", fg="white", width=15).pack()
Button(root, text="Sign Up", command=signup, bg="orange", fg="white", width=15).pack(pady=10)

root.mainloop()
