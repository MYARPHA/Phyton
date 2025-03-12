def multiplyElements(lst: list, multiplier = -1):
    return [element * multiplier for element in lst]

print(multiplyElements([5, 6], 2))
