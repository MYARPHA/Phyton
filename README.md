
root.bind_class("Entry", "<Button-1>", lambda event: on_left_click(event, "Поле ввода"))
root.bind_class("Entry", "<Button-2>", lambda event: on_right_click(event, "Поле ввода"))

entry1.bind("<Button-1>", lambda event: on_left_click(event, "Поле ввода 1"))
entry1.bind("<Button-2>", lambda event: on_right_click(event, "Поле ввода 1"))

entry2.bind("<Button-1>", lambda event: on_left_click(event, "Поле ввода 2"))
entry2.bind("<Button-2>", lambda event: on_right_click(event, "Поле ввода 2"))

entry3.bind("<Button-1>", lambda event: on_left_click(event, "Поле ввода 3"))
entry3.bind("<Button-2>", lambda event: on_right_click(event, "Поле ввода 3"))
