import math
def y(x):
    if x < -10:
        return round(math.pi * x**2, 3)
    elif -10 <= x < -5:
        return round(x**2, 3)
    elif -5 <= x < 10:
        return round(math.e * abs(x), 3)
    elif x >= 10:
        return round(1 / math.sin(math.sqrt(x)), 3)

x = float(input("Введите число x: "))
result = y(x)
print(f"Значение функции y(x) = {result}")