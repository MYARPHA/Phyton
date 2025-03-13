import os

fileName = input("Введите имя файла: ")

if os.path.exists(fileName):
    appendOrOverwrite = input("Файл существует. Хотите дописать в конец (a) или перезаписать (w)? (a/w): ")
    mode = 'a' if appendOrOverwrite == 'a' else 'w'
else:
    mode = 'w' # если файл не существует
with open(fileName, mode) as file:
    print("Введите текст. Для завершения введите end.")
    while True:
        userInput = input()
        if userInput == 'end':
            break
        file.write(userInput + '\n')