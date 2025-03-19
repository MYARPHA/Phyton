import psutil
import os
import subprocess


def list_processes():
    print("PID\tИмя процесса")
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"{proc.info['pid']}\t{proc.info['name']}")


def start_program(path):
    try:
        subprocess.Popen(path)
        print(f"Программа {path} запущена.")
    except Exception as e:
        print(f"Ошибка запуска программы: {e}")


def kill_process(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
        print(f"Процесс {pid} завершён.")
    except psutil.NoSuchProcess:
        print("Процесс не найден.")
    except Exception as e:
        print(f"Ошибка завершения процесса: {e}")


def main():
    while True:
        print("\n1. Показать процессы")
        print("2. Запустить программу")
        print("3. Завершить процесс")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            list_processes()
        elif choice == "2":
            path = input("Введите путь к исполняемому файлу: ")
            start_program(path)
        elif choice == "3":
            try:
                pid = int(input("Введите PID процесса: "))
                kill_process(pid)
            except ValueError:
                print("Введите корректный числовой PID.")
        elif choice == "4":
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()