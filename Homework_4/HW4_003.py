# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

import random
num = input('Введите натуральное число больше 0: ')
while not (num[0] != '0' and num.isdigit()):  # проверка на число
    num = input('Введите натуральное число больше 0: ')
num = int(num)
numbers = [random.randint(0, num) for item in range(0, num)]
print(f'Cписок чисел: {numbers}')
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(f'Cписок уникальных чисел: {unique}')
