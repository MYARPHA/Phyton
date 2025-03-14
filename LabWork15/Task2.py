import tkinter as tk

def onLeftClick(event, fieldName):
    label.config(text=f"Активное поле: {fieldName}")

def onRightClick(event, fieldName):
    print(f"Правый клик на поле: {fieldName}")

root = tk.Tk()
root.geometry("400x300")
root.title("Оконное приложение с полями ввода")

# Метка для отображения активного поля
label = tk.Label(root, text="Активное поле: ", height=2)
label.pack()

# Создание трех полей ввода
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

entry3 = tk.Entry(root)
entry3.pack(pady=5)

root.bind_class("Entry", "<Button-1>", lambda event: onLeftClick(event, "Поле ввода"))
root.bind_class("Entry", "<Button-2>", lambda event: onRightClick(event, "Поле ввода"))

entry1.bind("<Button-1>", lambda event: onLeftClick(event, "Поле ввода 1"))
entry1.bind("<Button-2>", lambda event: onRightClick(event, "Поле ввода 1"))

entry2.bind("<Button-1>", lambda event: onLeftClick(event, "Поле ввода 2"))
entry2.bind("<Button-2>", lambda event: onRightClick(event, "Поле ввода 2"))

entry3.bind("<Button-1>", lambda event: onLeftClick(event, "Поле ввода 3"))
entry3.bind("<Button-2>", lambda event: onRightClick(event, "Поле ввода 3"))

root.mainloop()