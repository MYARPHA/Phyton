import tkinter as tk

def updateLabel():
    labelResult.config(text=f"{entryText.get()}, {varCheck.get()}, {varRadio.get()}")

root = tk.Tk()
root.geometry("300x200")
root.title("Связь")

entryText = tk.StringVar()
varCheck = tk.IntVar()
varRadio = tk.StringVar(value="Option 1")

tk.Entry(root, textvariable=entryText).pack()

tk.Checkbutton(root, text="Флажок", variable=varCheck).pack()

tk.Radiobutton(root, text="Вариант 1", variable=varRadio, value="Option 1").pack()
tk.Radiobutton(root, text="Вариант 2", variable=varRadio, value="Option 2").pack()

labelResult = tk.Label(root, text="")
labelResult.pack()

tk.Button(root, text="Обновить", command=updateLabel).pack()
root.mainloop()