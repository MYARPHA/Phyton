import os

fileName = input("Введите имя файла: ")

# Существует ли файл
if os.path.exists(fileName):
    # Содержимое файла(чтение)
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла: ")
            print(content)
    except Exception as e:
        print(f"Ошибка{e}")

    # Проверка расширения файла .py
    ext = os.path.splitext(fileName)
    if ext == '.py':
        try:
            print("Выполнение Python-скрипта из файла...")
            exec(content)
        except Exception as e:
            print(f"Ошибка{e}")
    else:
        print("Файл не являеться .py")
else:
    print("Файл не существует.")