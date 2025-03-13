import os

fileName = input("Введите имя файла: ")

if os.path.exists(fileName):
    with open(fileName, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()

    for line in lines:
        numbers = line.split()
        try:
            numbers = list(map(int, numbers))
            print(f"Сумма в строке: {sum(numbers)}")
        except ValueError:
            print("Ошбка")
else:
    print("Файл не существует")