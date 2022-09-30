# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2,2,2,2,2,3]->13

num = input('Введите натуральное число больше 0: ')
while not (num[0] !='0' and num.isdigit()):
    num = input('Введите натуральное число больше 0: ')
spisok=[round((1+1/n)**n) for n in range(1,int(num)+1)]
print (f'n = {num}: {spisok} -> {sum(spisok)}')