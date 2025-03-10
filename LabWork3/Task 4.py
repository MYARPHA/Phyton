def main():
    try:
        purchase = float(input("Введите сумму покупки: "))
    except ValueError:
        print("Ошибка!")
        return

    paid = 0.0

    while paid < purchase:
        try:
            amount = float(input("Введите внесённую сумму: "))
        except ValueError:
            print("Ошибка!")
            continue

        if amount <= 0:
            print("Ошибка!")
            continue

        paid += amount

        if paid < purchase:
            shortage = purchase - paid
            print(f"Недостаточно средств! Сумма доплаты: {shortage}")

    change = paid - purchase

    if change == 0.0:
        print("Спасибо!")
    else:
        print(f"Возьмите сдачу: {change}")

if __name__ == "__main__":
    main()