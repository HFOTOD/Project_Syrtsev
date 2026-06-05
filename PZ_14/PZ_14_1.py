from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Sign Up")
root.geometry("600x650")
root.configure(bg="#1d223d")

title = Label(root, text="Sign Up",
              bg="#d98b00", fg="white",
              font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=2,
           sticky="ew", pady=10)

Label(root, text="First Name", bg="#1d223d", fg="yellow").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="Last Name", bg="#1d223d", fg="yellow").grid(row=2, column=0, padx=10, pady=5)
Label(root, text="Screen Name", bg="#1d223d", fg="yellow").grid(row=3, column=0, padx=10, pady=5)
Label(root, text="Date of Birth", bg="#1d223d", fg="yellow").grid(row=4, column=0, padx=10, pady=5)
Label(root, text="Gender", bg="#1d223d", fg="yellow").grid(row=5, column=0, padx=10, pady=5)
Label(root, text="Country", bg="#1d223d", fg="yellow").grid(row=6, column=0, padx=10, pady=5)
Label(root, text="E-mail", bg="#1d223d", fg="yellow").grid(row=7, column=0, padx=10, pady=5)
Label(root, text="Phone", bg="#1d223d", fg="yellow").grid(row=8, column=0, padx=10, pady=5)
Label(root, text="Password", bg="#1d223d", fg="yellow").grid(row=9, column=0, padx=10, pady=5)
Label(root, text="Confirm Password", bg="#1d223d", fg="yellow").grid(row=10, column=0, padx=10, pady=5)

first_name = Entry(root, width=35)
last_name = Entry(root, width=35)
screen_name = Entry(root, width=35)

first_name.grid(row=1, column=1, pady=5)
last_name.grid(row=2, column=1, pady=5)
screen_name.grid(row=3, column=1, pady=5)

frame_date = Frame(root, bg="#1d223d")
frame_date.grid(row=4, column=1, pady=5)

months = ttk.Combobox(frame_date, values=[
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
], width=10)

days = ttk.Combobox(frame_date,
                    values=list(range(1, 32)),
                    width=5)

years = ttk.Combobox(frame_date,
                     values=list(range(1950, 2025)),
                     width=8)

months.current(0)
days.current(0)

months.pack(side=LEFT, padx=5)
days.pack(side=LEFT, padx=5)
years.pack(side=LEFT, padx=5)

gender = StringVar(value="Male")

Radiobutton(root, text="Male",
            variable=gender, value="Male",
            bg="#1d223d", fg="yellow").grid(row=5, column=1, sticky="w")

Radiobutton(root, text="Female",
            variable=gender, value="Female",
            bg="#1d223d", fg="yellow").grid(row=5, column=1)

country = ttk.Combobox(root,
                       values=["USA", "Canada", "Germany", "France", "Russia"],
                       width=32)
country.current(0)
country.grid(row=6, column=1, pady=5)

email = Entry(root, width=35)
phone = Entry(root, width=35)
password = Entry(root, width=35, show="*")
confirm_password = Entry(root, width=35, show="*")

email.grid(row=7, column=1, pady=5)
phone.grid(row=8, column=1, pady=5)
password.grid(row=9, column=1, pady=5)
confirm_password.grid(row=10, column=1, pady=5)

agree = IntVar()

Checkbutton(root,
            text="I agree to the Terms of Use",
            variable=agree,
            bg="#1d223d",
            fg="yellow").grid(row=11, column=1, sticky="w", pady=10)

def submit():
    if password.get() != confirm_password.get():
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if agree.get() == 0:
        messagebox.showwarning("Warning",
                               "You must agree to the Terms of Use")
        return

    messagebox.showinfo("Success",
                        "Registration completed!")

Button(root,
       text="Submit",
       bg="lightgreen",
       command=submit).grid(row=12, column=1, sticky="w", pady=20)

Button(root,
       text="Cancel",
       bg="tomato",
       command=root.destroy).grid(row=12, column=1, sticky="e", pady=20)

root.mainloop()
