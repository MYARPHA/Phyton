sec = int(input("Введите количество секунд: "))
secondInDay = 86400

# отбрасыване лишних секунд
sec = sec % secondInDay

# Количество часов, минут и секунд
hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")