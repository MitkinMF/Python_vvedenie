# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число: ')
while not num.lstrip('-').replace('.', '', 1).isdigit():
    num = input('Введите вещественное число: ')
print(sum(list(map(int, num.lstrip('-').replace('.', '', 1)))))
