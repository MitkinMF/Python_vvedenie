# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных
# числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5 -> [-5, -4,-3,-2,-1,0,1,2, 3, 4,5]
# -> 15

def user_input():
    num = input('Введите натуральное число больше 0: ')
    while not (num[0] != '0' and num.isdigit()):
        num = input('Введите натуральное число больше 0: ')
    return int(num)

print('Input position one')
pos_one = user_input()
print('Input position two')
pos_two = user_input()

if pos_two < pos_one:
    n = pos_one + 2
else:
    n = pos_two + 2

spisok = [item for item in range(-n, n + 1)]

print(f'Position one: {pos_one}')
print(f'Position two: {pos_two}')
print(f'Number of elements: {n} -> {spisok}')
print(f'-> {spisok[pos_one - 1]*spisok[pos_two - 1]}')
