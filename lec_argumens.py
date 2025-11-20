def my_func(a, b):
    x = 3 * a - b
    return x

# tmp = my_func() # TypeError: my_func() missing 2 required positional arguments: 'a' and 'b' - функция ожидает 2 аргумента

def my_func(a=1, b=2): # значения по умолчанию для аргументов функции
     
     x = 3 * a - b
     return x

print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=9))
print(my_func(b=3, a=9))

def my_func(a, b=0):
     x = 3 * a - b
     return x

def my_func(*args): # * запаковка в кортеж(занимает мало места)
     x = 3 * (args[0] - args[1])
     return x

print(my_func(3,4))
print(my_func(3, 4, 8))

def my_func(**kwrgs): # ** запаковка в словарь
     x =  3 * kwrgs['obj_1'] - kwrgs['obj_2']
     return x
print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3 = 8))


def final_func(a: float, b: int=1, c=4, *arg,  ** kw): # флоат -- рекомендация
    print(f'Hello World {a} + {b} + {c} - {arg} / {kw}')

final_func(1)
final_func(1, 4)
final_func(1,4, 6)
final_func(1,4, 6, 'fhtg',4 , 8)
final_func(1, f=5, h='Good')
final_func


 