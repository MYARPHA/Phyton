import re

text = "ТЫ редиска! Ты вообще нехороший человек. И они тоже редиски РЕДИСКИ!"

pattern = r'\bредиск[аио]?|\bнехороший( человек)?\b'

# Замена
result = re.sub(pattern, 'давайте жить дружно', text, flags = re.IGNORECASE)

print(result)
