import os

fileName = input("Введите имя файла: ")

if os.path.exists(fileName):
    print("Выберите опцию: ")
    print("1. Вывести содержимое файла")
    print("2. Удалить файл")
    print("3. Переименовать файл")

    choice = input("Ваш выбор (1/2/3): ")

    if choice == '1':
        with open(fileName, 'r', encoding='utf-8') as file:
            print(file.read())
    elif choice == '2':
        os.remove(fileName)
        print("Файл удалён")
    elif choice == '3':
        newName = input("Введите новое имя файла: ")
        os.rename(fileName, newName)
        print(f"Файл {fileName} переименован в {newName}")