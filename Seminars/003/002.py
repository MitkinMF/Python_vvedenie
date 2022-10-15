# 2.Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

my_list = ['uff' , '32' , '7kw', ' 0ksl']

num = input("Введите искомое число: ")

for elem in my_list:
    if num in elem:
        print(True)
        break
else:
    print(False)
