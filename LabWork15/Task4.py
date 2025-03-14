import tkinter as tk

def updateKey(event):
    label.config(text=f"Нажатые клавиши: {event.char}")

root = tk.Tk()
root.geometry("400x300")
root.title("Нажатые клавиши")

label = tk.Label(root, text="Нажатые клавиши: ", height=2)
label.pack()

root.bind("<Key>", updateKey)

root.mainloop()