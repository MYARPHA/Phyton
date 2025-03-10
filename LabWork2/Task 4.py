a, b, c = map(int, input("Введите три стороны треугольника(ЧЕРЕЗ ПРОБЕЛ): ").split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        triangleType = "Равносторонний"
    elif a == b or a == c or b == c:
        triangleType = "Равнобедренный"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        triangleType = "Прямоугольный"
    else:
        triangleType = "Разносторонний"
    print(f"Можно построить треугольник: {triangleType}")
else:
    print("Нельзя построить треугольник!")