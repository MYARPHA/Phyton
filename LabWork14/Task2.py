import tkinter as tk


def register():
    login = entryLogin.get()
    password = entryPassword.get()
    varGender = gender.get()
    about = textAbout.get("1.0", tk.END) #1.0 первый символ в строке

    selctedIndex = continentLst.curselection() #индекс выделенного материка
    if selctedIndex:
        continent = continents[selctedIndex[0]] #получаем название по индексу
    else:
        continent = "Не выбран"

    print(f"Логин: {login}, Пароль: {password}, Пол: {varGender}, Материк: {continent}, О себе: {about}")

root = tk.Tk()
root.geometry("300x500")
root.title = ("Форма регистрации")

tk.Label(root, text="Логин", bg="#FFE4E1").pack()
entryLogin = tk.Entry(root)
entryLogin.pack()

tk.Label(root, text="Пароль", bg="#FFE4E1").pack()
entryPassword = tk.Entry(root, show = "*")
entryPassword.pack()


tk.Label(root, text="О себе", bg="#FFE4E1").pack()
textAbout = tk.Text(root, height=5)
textAbout.pack()

gender = tk.StringVar(value="Мужской")
tk.Label(root, text="Пол", bg="#FFE4E1").pack()
tk.Radiobutton(root, text="Мужской", variable=gender, value="Мужской", bg="#FFE4E1").pack()
tk.Radiobutton(root, text="Женский", variable=gender, value="Женский", bg="#FFE4E1").pack()

tk.Label(root, text = "Материк", bg="#FFE4E1").pack()
continentLst = tk.Listbox(root)
continents = ["Европа", "Азия", "Африка", "Америка", "Австралия"]

for continent in continents:
    continentLst.insert(tk.END, continent)
continentLst.pack()

tk.Button(root, text="Зарегистрироваться", command=register).pack()

root.mainloop()

