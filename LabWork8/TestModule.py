import HelloModule
import TextProcessingModule
import ConversionModule
import CaesarCipherModule
import BiteOperationModule

HelloModule.hello("JOOST KLIEN TOMMY CASH BOULEVARD DEPO")

print("Перевод числа 255 в двоичную систему:", ConversionModule.decimal_to_base(255, 2))

text = "Это первое предложение. Это второе предложение."
TextProcessingModule.print_sentences(text)

print("Шифр Цезаря:", CaesarCipherModule.caesar_cipher("Hello, World!", 3))

print("Битовое И 5 и 3:", BiteOperationModule.bitwise_and(5, 3))
print("Битовое ИЛИ 5 и 3:", BiteOperationModule.bitwise_or(5, 3))
print("Битовое XOR 5 и 3:", BiteOperationModule.bitwise_xor(5, 3))
print("Битовое НЕ 5:", BiteOperationModule.bitwise_not(5))