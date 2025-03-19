try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    result = a / b
    print("Результат деления:", result)
except ZeroDivisionError:
    print("Ошибка: деление на 0 невозможно.")