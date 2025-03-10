number = float(input("Введите число: "))
# До 3х знаков после ,
print("Округление до 3х знаков: {:.3f}".format(number))

# До N знаков через метод Round
numb =int(input("Введите количество знаков после запятой: "))
print("Округление до {} знаков числа: {}".format(numb, round(number, numb)))