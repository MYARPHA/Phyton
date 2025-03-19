import random

# 5.1
string = input("Введите строку: ")
print((string + '\n') * 5)
print(f"Длина строки: {len(string)}")
for i, char in enumerate(string):
    print(f"{i}: {char}")
print("Каждый второй символ:")
for i in range(1, len(string), 2):
    print(f"Позиция {i + 1}: {string[i]}")

# 5.2
start = int(input("Введите начальную позицию: "))
end = int(input("Введите конечную позицию: "))
print(string[start:end])

# 5.3
modified_string = "#" + string[1:-1] + "#"
print(modified_string)

# 5.4
if string.isdigit():
    print("Строка состоит только из цифр")
elif string.isalpha():
    if string.islower():
        print("Строка состоит только из строчных букв")
    elif string.isupper():
        print("Строка состоит только из прописных букв")
    else:
        print("Строка состоит из букв разных регистров")
elif string.isalnum():
    print("Строка состоит из букв и цифр")
else:
    print("Строка содержит другие символы")

# 5.5
words = string.split()
print(", ".join(words))

# 5.6
sub_string = input("Введите подстроку для поиска: ")
count = string.count(sub_string)
print(f"Подстрока встречается {count} раз")
index = -1
while True:
    index = string.find(sub_string, index + 1)
    if index == -1:
        break
    print(f"Найдено на позиции {index}")

# 5.7
if string.lower() == string.lower()[::-1]:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

# 5.8
print(" ".join(string.split()))

# 5.9
correct_answer = "Python"
user_answer = input("Введите ответ: ").strip().lower()
if user_answer == correct_answer.lower():
    print("Ответ верный")
else:
    print("Ответ неверный")
