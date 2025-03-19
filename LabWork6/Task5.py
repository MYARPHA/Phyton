books = {}
while True:
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Просмотреть список книг")
    print("4. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        books[title] = author
    elif choice == "2":
        title = input("Введите название книги для удаления: ")
        try:
            del books[title]
            print("Книга удалена.")
        except KeyError:
            print("Ошибка: такой книги нет в списке.")
    elif choice == "3":
        if books:
            for title, author in books.items():
                print(f"{title} - {author}")
        else:
            print("Список книг пуст.")
    elif choice == "4":
        break
    else:
        print("Некорректный ввод.")
