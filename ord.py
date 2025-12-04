# Функция ord переводит символы в их ASCII коды , каждому символу соответствует ASCII код
# А функция chr производит обратную операцию

text = "Hello"

for symbol in text:
    print(ord(symbol), end="; ")
print()

print(chr(14456))