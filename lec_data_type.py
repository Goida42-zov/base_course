x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)

print(z + w)

#Strings - строки
s = 'Hello'
print(s[0])

# s[0] = 'H'
# Tumple - кортеж
t = (1, 4, 9)
print(t)
print(t[0])
 # t[0] = 3 т.к. кортеж неизменяемый тип данных
# Dict - словарь
d = {'key_1': 4, 2: 'red', 'str': 'hello'}
print(d['key_1'])
print(d[2])
print(d['str'])

d['str'] = 'world' # т.к. словарь изменяемый тип данных
print(d['str'])
print(d)