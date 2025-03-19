import os
import datetime

def create_file(filename):
    with open(filename, 'w') as f:
        f.write("")
    print(f"Файл '{filename}' создан.")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"Файл '{filename}' удалён.")
    except FileNotFoundError:
        print("Файл не найден.")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            text = input("Введите текст для добавления: ")
            f.write(text + "\n")
        print("Файл обновлён.")
    except FileNotFoundError:
        print("Файл не найден.")

def search_files(extension=None, min_size=0, max_size=float('inf'), date=None):
    files = os.listdir()
    result = []
    for file in files:
        if os.path.isfile(file):
            stat = os.stat(file)
            size = stat.st_size
            mod_time = datetime.datetime.fromtimestamp(stat.st_mtime).date()
            if ((not extension or file.endswith(extension)) and
                (min_size <= size <= max_size) and
                (not date or mod_time == date)):
                result.append(file)
    print("Найденные файлы:", result)

def main():
    while True:
        print("\nФайловый менеджер:")
        print("1. Создать файл")
        print("2. Удалить файл")
        print("3. Изменить файл")
        print("4. Найти файлы")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите имя файла: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Введите имя файла: ")
            delete_file(filename)
        elif choice == '3':
            filename = input("Введите имя файла: ")
            edit_file(filename)
        elif choice == '4':
            ext = input("Введите расширение файла (например, .txt), или оставьте пустым: ")
            min_size = int(input("Минимальный размер (в байтах): ") or 0)
            max_size = int(input("Максимальный размер (в байтах): ") or float('inf'))
            date_str = input("Введите дату изменения (YYYY-MM-DD) или оставьте пустым: ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
            search_files(ext, min_size, max_size, date)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()
