a, b, c = map(int, input("Введите три числа(ЧЕРЕЗ ПРОБЕЛ): ").split())

middleNumb = a if (b < a < c or c < a < b) else b if (a < b < c or c < b < a) else c

print(f"Среднее число: {middleNumb}")
