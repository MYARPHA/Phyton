def analyze(*args):
    if len(args) == 0:
        print("Нет чисел для анализа")
        return

    totalSum = sum(args)
    average = totalSum / len(args)
    maximum = max(args)
    minimum = min(args)
    
    print(f"Количество чисел: {len(args)}")
    print(f"Сумма: {totalSum}")
    print(f"Среднее значение: {average}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")

    

print("Несколько чисел: ")
analyze(10, 20, 30, 40)

print("Одно число: ")
analyze(40)

print("Без чисел: ")
analyze()
