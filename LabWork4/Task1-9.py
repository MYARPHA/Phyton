import random

# 5.1
n = int(input("Введите количество элементов списка: "))
list1 = [random.randint(0, 100) for _ in range(n)]
for i, val in enumerate(list1):
    print(f"{i}: {val}")

# 5.2
n = int(input("Введите количество элементов списка: "))
list2 = [input(f"Введите элемент {i+1}: ") for i in range(n)]
print(" ".join(list2))

# 5.3
list1.extend([x for x in list2 if isinstance(x, int) and x % 2 == 0])
print(" ".join(map(str, list1)))

# 5.4
print(" ".join(map(str, list1[::-1])))

# 5.5
num = int(input("Введите число для поиска: "))
count = list1.count(num)
print(f"Количество совпадений: {count}")
list1 = [x for x in list1 if x != num]
print(" ".join(map(str, list1)))

# 5.6
n = int(input("Введите количество вставляемых элементов: "))
for _ in range(n):
    index = int(input("Введите индекс: "))
    value = int(input("Введите значение: "))
    list1.insert(index, value)
print(" ".join(map(str, list1)))

# 5.7
math_scores = [random.randint(50, 100) for _ in range(15)]
russian_scores = [random.randint(50, 100) for _ in range(15)]
informatics_scores = [random.randint(50, 100) for _ in range(15)]
names = [f"Абитуриент_{i+1}" for i in range(15)]
total_scores = [(i, names[i], math_scores[i] + russian_scores[i] + informatics_scores[i]) for i in range(15)]
total_scores.sort(key=lambda x: x[2], reverse=True)
accepted = total_scores[:10]
for index, name, _ in accepted:
    print(f"{index}: {name}")

# 5.8
my_dict = {"ключ1": "значение1", "ключ2": "значение2", "ключ3": "значение3"}
print("Ключи:", list(my_dict.keys()))
print("Значения:", list(my_dict.values()))
key = input("Введите ключ: ")
print(my_dict.get(key, "Ключ не найден"))

# 5.9
regions = {
    "Архангельская область": ["Архангельск", "Новодвинск", "Северодвинск", "Шенкурск", "Котлас"],
    "Ленинградская область": ["Санкт-Петербург", "Пушкин", "Павловск"]
}
cities = [input("Введите город: ") for _ in range(3)]
for city in cities:
    for region, city_list in regions.items():
        if city in city_list:
            print(region)
