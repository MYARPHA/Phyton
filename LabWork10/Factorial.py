def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



n = int(input("Введите число: "))
fact = factorial(n)
print(f"Факторал числа {n} = {fact}")

# Подсказка! n(next), s(step), p name(print), q(quit)
# s - внутрь factorial (пошаговое)
# n - без захода в функцию