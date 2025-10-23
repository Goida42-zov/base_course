for i in 1, 3, 4:
    print(i**2, end = ' ')#пробелы

for i in 1,3,4:
    print(i**2, end='\n') #ЛИТЕР

for i in 1, 3, 4:
    print(i, i**2, sep =' -> ') #сепаратор

a = [1, 5, 7, 10]
for i in a:
    print(f'{i}**3 = {i**3}') # через f строку