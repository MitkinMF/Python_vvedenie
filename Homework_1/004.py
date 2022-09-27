# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

flag = True
while flag:
    quater = input('Введите номер координатной четверти: ')
    if len(quater) == 1:
        if not (1 <= int(quater) <= 4):
            print('Числа должны быть от 1 до 4')
        else:
            flag = not flag
if quater == 1:
    print('х>0, y>0')
elif quater == 2:
    print('х<0, y>0')
elif quater == 3:
    print('х<0, y<0')
else:
    print('х>0, y<0')

