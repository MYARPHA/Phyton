while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        if b == 0:
            raise ValueError("0 вводить нельзя, попробуйте снова.")
        result = a / b
    except ValueError as e:
        print(e)
    else:
        break
    finally:
        print("Результат деления:", result)
