# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def user_input():
    flag = True
    while flag:
        cord = input('два числа через пробел:').split()
        if len(cord) == 2:
            x, y = float(cord[0]), float(cord[1])
            flag = not flag
    return x, y

print('Введите координаты точки A')
x_a, y_a = user_input()
print('Введите координаты точки B')
x_b, y_b = user_input()

dist=int((((x_b-x_a)**2+(y_b-y_a)**2)**0.5)*100)/100

print(dist)
