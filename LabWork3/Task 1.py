import random

# проверка случайного числа
def isPrime(n):
    if n < 2:
        return False # если число < 2 - не простое
    for i in range(2, int(n**0.5) + 1): # делители от 2 до n под корнем
        if n % i == 0: # если хотя бы одно число  делит n без остатка, n - не простое
            return False
        return True
# генерация
number = random.randint(1, 1000)
print(f"Случайное число: {number}")
print("Простое" if isPrime(number) else "Не простое")