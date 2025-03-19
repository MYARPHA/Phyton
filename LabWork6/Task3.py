import math
try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))
    numerator = math.sqrt(x + y + z)
    denominator = (x - y + z) ** 2
    result = numerator / denominator
    print("Результат вычисления:", result)
except ValueError:
    print("Ошибка: введены некорректные данные.")
except ZeroDivisionError:
    print("Ошибка: деление на 0 невозможно.")
