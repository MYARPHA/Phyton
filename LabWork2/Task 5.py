a, b = map(int, input("Введите 2 целых числа: ").split())
operation = input("Введите операцию: ".lower())

result = (a & b if operation == "и" else
          a | b if operation == "или" else
          a ^ b if operation == "исключающее или" else
          a << b if operation == "сдвиг влево" else
          a >> b if operation == "сдвиг вправо" else
          "ОШИБКА ПЕРЕДЕЛЫВАЙ")

if isinstance(result, int):
    print(f"{a:08b} ({a}) {operation} {b:08b} ({b}) = {result:08b} ({result})") # 08b - перебор в 8ми битное двоичное представление
else:
    print(result)
