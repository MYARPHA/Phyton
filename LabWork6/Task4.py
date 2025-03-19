import math

try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))
    if x + y + z < 0:
        raise ValueError("Ошибка: под корнем отрицательное число.")
    numerator = math.sqrt(x + y + z)
    denominator = (x - y + z) ** 2
    result = numerator / denominator
    print("Результат вычисления:", result)
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Ошибка: деление на 0 невозможно.")