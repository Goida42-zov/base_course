for symbol in 'hello world':
    if symbol == 'o':
       break # останровмит цикл
    print(symbol)

for symbol in 'hello world':
    if symbol == 'o' or symbol == 'l':
        continue # пропустить текущую итерацию
    print(symbol)