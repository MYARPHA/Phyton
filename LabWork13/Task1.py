import json

fruits = [
    {"name": "Апельсин", "price": 80},
    {"name": "Яблоко", "price": 50},
    {"name": "Бананчик", "price": 60}
]

with open("fruits.json", "w", encoding="utf-8") as file:
    json.dump(fruits, file, ensure_ascii=False, indent=4)
print("Файл JSON создан!")