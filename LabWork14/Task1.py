import tkinter as tk

def login():
    print(f"Логин: {entryLogin.get()}, Пароль: {entryPassword.get()}, Запонить: {remember.get()}")

root = tk.Tk()
root.geometry("200x300")
root.title("Форма авторизации")

tk.Label(root, text="Логин").pack() #pack()-размещение метки в окне
entryLogin = tk.Entry(root)
entryLogin.pack()

tk.Label(root, text="Пароль").pack()
entryPassword = tk.Entry(root, show = "*")
entryPassword.pack()

remember = tk.BooleanVar()
tk.Checkbutton(root, text = "Запомнить пароль", variable = remember).pack()

tk.Button(root, text = "Авторизоваться", command = login).pack()

root.mainloop()