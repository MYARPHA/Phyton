from calendar import month, isleap

year, month = map(int, input("Введите год и номер месяца (ЧЕРЕЗ ПРОБЕЛ): ").split())

isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days = 29 if (month == 2 and isLeap) else 28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31 if month in [1, 3, 5, 7, 8, 10, 12] else "Такого месяца нет!"

print(f"Количество дней в месяце: {days}")