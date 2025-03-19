def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr(shift_base + (ord(char) - shift_base + shift) % 26)
        else:
            result += char
    return result