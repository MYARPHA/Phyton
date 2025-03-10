import random
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

randomNumb = random.uniform(a, b)

print("Случайное число от {} до {}: {:.2f}".format(a,b, randomNumb))