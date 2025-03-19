class Author:
    def __init__(self, full_name, country):
        self.full_name = full_name
        self.country = country

    def display_info(self):
        print(f"Автор: {self.full_name}, Страна: {self.country}")


class Book:
    def __init__(self, title):
        self.__content = []
        self.title = title
        print(f"Книга '{self.title}' создана")

    def __del__(self):
        print(f"Книга '{self.title}' удалена")

    def add_work(self, work):
        self.__content.append(work)

    def get_work_count(self):
        return len(self.__content)

    def display_info(self):
        print(f"Книга: {self.title}\nСодержание:")
        for i, work in enumerate(self.__content, 1):
            print(f"{i}) {work}")


class AuthorBook(Author, Book):
    def __init__(self, full_name, country, title):
        Author.__init__(self, full_name, country)
        Book.__init__(self, title)

    def display_full_info(self):
        print(f"Автор: {self.full_name}, Страна: {self.country}")
        self.display_info()


n = int(input("Введите количество авторов: "))
authors = []

for _ in range(n):
    name = input("Введите ФИО автора: ")
    country = input("Введите страну автора: ")
    authors.append(Author(name, country))

title = input("Введите название книги: ")
book = AuthorBook(authors[0].full_name, authors[0].country, title)

while True:
    work = input("Введите произведение (или 'стоп' для завершения): ")
    if work.lower() == 'стоп':
        break
    book.add_work(work)

print("\nСписок всех авторов:")
for author in authors:
    author.display_info()

print("\nСписок русских авторов:")
for author in authors:
    if author.country.lower() == "россия":
        author.display_info()

print("\nИнформация о книге:")
book.display_full_info()
