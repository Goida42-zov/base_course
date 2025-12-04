# Списковые включения - listcomp - на выходе получаем список
# (хранит в себе все значения сразу):
symbols = 'Python'
symbols_codes = [ord(symbol)  for symbol in symbols ] # цикл внутри списка, котрый генерирует этот список
print(symbols_codes)


# Генераторные выражения - genexp - на выходе получаем
# объект-генератор (вычисляет значения по порядку):
symbols = '132'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes) # Объект-генератор


for object in symbol_codes:
    print(object) 


symbols = 'asd'
symbol_codes = (symbol for symbol in symbols)
print(symbol_codes) # Объект-генератор