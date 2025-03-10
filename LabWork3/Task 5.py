N = int(input("Введите количество значений N: "))
a = float(input("Введите коэффицент a: "))
b = float(input("Введите коэффицент b: "))
x1 = float(input("Введите начало отрезка x1: "))
x2 = float(input("Введите начало отрезка x2: "))

# определение шага
step = abs(x2 - x1) / (N - 1)
if x1 > x2:
    step = -step # обртаное направление

# вычисление значений
for i in range(N):
    x = x1 + i * step
    y = a * x + b
    print(f"y({x:.3f}) = {a} * {x:.3f} + {b} = {y:.3f}")