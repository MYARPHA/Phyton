def factorial(n: "число для вычисления факториала") -> int:
    if not isinstance(n, int):
        return -1
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(-1))
print(factorial(0))
