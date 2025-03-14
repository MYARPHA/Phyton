Привязка событий ко всем полям ввода с использованием bind_class
root.bind_class("Entry", "<Button-1>", lambda event: on_left_click(event, "Поле ввода"))
root.bind_class("Entry", "<Button-2>", lambda event: on_right_click(event, "Поле ввода"))

# Привязка конкретных полей ввода с указанием их имён
entry1.bind("<Button-1>", lambda event: on_left_click(event, "Поле ввода 1"))
entry1.bind("<Button-2>", lambda event: on_right_click(event, "Поле ввода 1"))

entry2.bind("<Button-1>", lambda event: on_left_click(event, "Поле ввода 2"))
entry2.bind("<Button-2>", lambda event: on_right_click(event, "Поле ввода 2"))

entry3.bind("<Button-1>", lambda event: on_left_click(event, "Поле ввода 3"))
entry3.bind("<Button-2>", lambda event: on_right_click(event, "Поле ввода 3"))
