# filter() - применяет другую функцию к заданному итерируемому
# объекту, проверяя, нужно ли сохранить конкретный элемент или нет
names = ["John", "David", "Maria", "Richard"]
ages = [12, 43, 52, 187]


def checker(user):
    name, age = user
    return age > 21
 
 
users = list(zip(names, ages))
canDrinkAlcohol = list(filter(checker, users))
print(canDrinkAlcohol)