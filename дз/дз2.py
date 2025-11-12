a1 = float(input("Введите первый член прогрессии: "))
q = float(input("Введите знаменатель прогрессии: "))
n = int(input("Введите количество членов прогрессии: "))

for i in range(n):
    an = a1 * q ** i
    print(an)
