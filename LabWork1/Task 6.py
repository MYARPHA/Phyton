year = int(input("Введите год: "))

isLeap = (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)
print(isLeap)