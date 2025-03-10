a = int(input("Введте первое число: "))
b = int(input("Введте второе число: "))

print(f"a + b = {a + b}") # f - для использования {}
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}"
      if b != 0 else "Деление на 0")
# Целая часть от деления
print(f"a // b = {a // b}"
      if b != 0 else "Деление на 0")
# Остаток от деления
print(f"a % b = {a % b}"
      if b != 0 else "Деление на 0")
# Возведение в степень
print(f"a ** b = {a ** b}")

# min/max
print(f"min = {b if a > b else a}")
print(f"max = {a if b > b else b}")

# Task 2
print("{0} + {1} = {2}".format(a, b, a + b))
print("{0} - {1} = {2}".format(a, b, a - b))
print("{0} * {1} = {2}".format(a, b, a * b))
print("{0} / {1} = {2}".format(a, b, a / b) if b != 0 else "Деление на 0")
print("{0} // {1} = {2}".format(a, b, a // b) if b != 0 else "Деление на 0")
print("{0} ** {1} = {2}".format(a,b, a**b))

print("min = {}".format(min(a, b)))
print("max = {}".format(max(a, b)))