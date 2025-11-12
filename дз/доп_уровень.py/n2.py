a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("треугольник существует")

    if a == b == c:
        print("треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")

else:
    print("треугольник не существует")
