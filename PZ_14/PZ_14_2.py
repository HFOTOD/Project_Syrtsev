from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Практическая работа №2")
root.geometry("420x250")
root.resizable(False, False)


def calculate():
    try:
        n = int(entry.get())

        seconds_in_current_hour = n % 3600
        full_minutes = seconds_in_current_hour // 60

        result.config(text=f"Полных минут: {full_minutes}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число!")


def clear():
    entry.delete(0, END)
    result.config(text="")


Label(root,
      text="Введите количество секунд\nс начала суток",
      font=("Arial", 12)).pack(pady=10)

entry = Entry(root, width=30)
entry.pack()

Button(root,
       text="Вычислить",
       width=15,
       command=calculate).pack(pady=10)

result = Label(root,
               text="",
               font=("Arial", 12))
result.pack()

Button(root,
       text="Очистить",
       width=15,
       command=clear).pack(pady=5)

Button(root,
       text="Выход",
       width=15,
       command=root.destroy).pack()

root.mainloop()
