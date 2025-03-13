import re

text = "Привет! КАК ДЕЛА? Ау... эх."

pattern = r'[.!?...]+' # + жадюга(квантор) забирает макс возможное число символов

sentences = re.split(pattern, text)

# Удаление пустых строк
for sentence in sentences:
    if sentence.strip():
        print(sentence.strip()) #strip - удаление пробелов