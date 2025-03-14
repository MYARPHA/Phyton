import json

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def toJson(self):
        return {"name": self.name, "age": self.age, "color": self.color}

class CatsManager:
    fileName = "cats.json"

    @staticmethod
    def loadCat():
        try:
            with open(CatsManager.fileName, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def saveCats(cats):
        with open(CatsManager.fileName, "w", encoding="utf-8") as file:
            json.dump(cats, file, ensure_ascii=False, indent=4)

    @staticmethod
    def addCats(name, age, color):
        cats = CatsManager.loadCat()
        cats.append(Cat(name, age, color).toJson())
        CatsManager.saveCats(cats)
        print(f"Китик {name} добавлен")

    @staticmethod
    def listCats():
        cats = CatsManager.loadCat()
        if not cats:
            print("Котов нет..")
        else:
            for cat in cats:
                print(f"Имя: {cat['name']}, Возраст: {cat['age']}, Окрас: {cat['color']}")

    @staticmethod
    def deleteCats(name):
        cats = CatsManager.loadCat()
        newCats = [cat for cat in cats if cat["name"] != name] #перебор котов -> добавление кота в новый список, если его имя не совпадает с name
        if len(cats) == len(newCats):                           #если имя совпадает то этот кот не попадёт в новый список т.е БУДЕТ УДАЛЁН!
            print(f"Котик {name} не найден :( ")
        else:
            CatsManager.saveCats(newCats)
            print(f"Котик {name} удалён...")

    @staticmethod
    def sortCats(by = "name"):
        cats = CatsManager.loadCat()
        if by == "age":
            cats.sort(key=lambda x: x["age"])
        else:
            cats.sort(key=lambda x: x["name"])
        CatsManager.saveCats(cats)
        print(f"Список котов отсортирован {by}")

CatsManager.addCats("Буся", 9, "полосатый")
CatsManager.addCats("Упырь", 6, "рыжий")
CatsManager.addCats("Оззи", 3, "серый")
CatsManager.addCats("Веня", 2, "полосатый")
CatsManager.addCats("Лёля", 1, "трёхцветная")
CatsManager.addCats("Анфиса", 1, "полосатый")

print("Список котов: ")
CatsManager.listCats()

#print("Удалить котика(ты уверен?): ")
#CatsManager.deleteCats()

#print("Список после удаления котика(ты изверг!): ")
#CatsManager.listCats()

print("Сортировка котов...")
CatsManager.sortCats("age")
CatsManager.sortCats()




