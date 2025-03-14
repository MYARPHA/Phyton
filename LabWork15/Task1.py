import tkinter as tk
from tkinter import filedialog

def saveFile(event=None):
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filePath:
        with open(filePath, "w") as file:
            text = textArea.get("1.0", tk.END)
            file.write(text)

def onClose(event=None):
    root.quit()

root = tk.Tk()
root.geometry("400x300")
root.title("Задание 1")

# Многострочное поле ввода
textArea = tk.Text(root, wrap=tk.WORD, width=40, height=20)
textArea.pack()

saveButton = tk.Button(root, text="Сохранить", command=saveFile)
saveButton.pack()

root.bind("<Control-s>", lambda event: saveFile())
root.bind("<Escape>", onClose)

root.mainloop()