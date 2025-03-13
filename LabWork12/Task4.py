import os

fileName = input("Введите имя файла: ")

if os.path.exists(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 1. Первая строка
    print("Первая строка: ", lines[0] if len(lines) > 0 else "Файл пуст!")

    # 2. Пятая строка
    print("Пятая строка: ", lines[4] if len(lines) > 5 else "Пятая строк осутсвует!")

    # 3. Первые 5 строк
    print("Первые 5 строк: ")
    for i in range(min(5, len(lines))):
        print(lines[i].strip())

    # 4. Строки с s1-й по s2-ю
    s1 = int(input("Введите номер первой строки(начиная с 1): "))
    s2 = int(input("Введите номер последней строки(начиная с 1): "))
    print(f"Строки с {s1+1} по {s2+1}: ")
    for i in range(s1, min(s2+1, len(lines))):
        print(lines[i].strip())

    # 5. Все строки
    print("Весь файл: ")
    for line in lines:
        print(line.strip())