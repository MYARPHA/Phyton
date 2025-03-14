import tkinter as tk
from cProfile import label


def changeColor(color):
    root.configure(bg=color)

def changeSize(size):
    root.geometry(size)

root = tk.Tk()
root.geometry("400x300")
root.title("Меню")

menu = tk.Menu(root)
root.config(menu=menu)

colorMenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Цвета", menu=colorMenu)
colorMenu.add_command(label="Красный", command=lambda: changeColor("red"))
colorMenu.add_command(label="Синий", command=lambda: changeColor("blue"))
colorMenu.add_command(label="Зелёный", command=lambda: changeColor("green"))

sizeMenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Размер", menu=sizeMenu)
sizeMenu.add_command(label="500x500", command=lambda: changeSize("500x500"))
sizeMenu.add_command(label="200x200", command=lambda: changeSize("200x200"))

root.bind("<Control-r>", lambda event: changeColor("red"))
root.bind("<Control-g>", lambda event: changeColor("green"))
root.bind("<Control-b>", lambda event: changeColor("blue"))
root.bind("<Control-q>", lambda event: changeSize("500x500"))
root.bind("<Control-w>", lambda event: changeSize("200x200"))

root.mainloop()