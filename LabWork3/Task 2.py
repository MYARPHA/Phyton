import random
number = random.randint(1, 10)
while True:
    guess = int(input("Угадай число от 1 до 10 хихихи: "))
    if guess == number:
        print("ТЫ УГАДАЛ!")
        break
    elif guess < number:
        print("Загаданое число больше!")
    else:
        print("Загаданое число меньше!")