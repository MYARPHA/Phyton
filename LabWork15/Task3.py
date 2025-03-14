import tkinter as tk

def updateCoord(event):
    label.config(text=f"Координаты мыши: x = {event.x}, y = {event.y}")

root = tk.Tk()
root.geometry("400x300")
root.title("Координаты мыши")

label = tk.Label(root, text="Координаты маши: x = 0, y = 0", height=2)
label.pack()

root.bind("<Motion>", updateCoord)

root.mainloop()