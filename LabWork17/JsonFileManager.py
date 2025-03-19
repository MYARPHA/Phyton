import os
import json

def create_file(path):
    with open(path, 'w') as f:
        pass
    print(f"Файл {path} создан.")


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"Файл {path} удален.")
    else:
        print(f"Файл {path} не найден.")


def create_folder(path):
    os.makedirs(path, exist_ok=True)
    print(f"Папка {path} создана.")


def delete_folder(path):
    if os.path.exists(path):
        os.rmdir(path)
        print(f"Папка {path} удалена.")
    else:
        print(f"Папка {path} не найдена.")


def rename(old_path, new_path):
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"{old_path} переименован в {new_path}.")
    else:
        print(f"{old_path} не найден.")


def execute_commands(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        commands = json.load(f)

    for command in commands:
        if command["command"] == "create_file":
            create_file(command["path"])
        elif command["command"] == "delete_file":
            delete_file(command["path"])
        elif command["command"] == "create_folder":
            create_folder(command["path"])
        elif command["command"] == "delete_folder":
            delete_folder(command["path"])
        elif command["command"] == "rename":
            rename(command["old_path"], command["new_path"])
        else:
            print(f"Неизвестная команда: {command['command']}")


if __name__ == "__main__":
    json_file = input("Введите путь к JSON-файлу: ")
    execute_commands(json_file)