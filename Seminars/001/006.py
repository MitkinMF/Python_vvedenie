# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81
from random import randint #импортируется модуль randint из random

for _ in range(int(input('введите число: '))): 
    print (randint(0,100),end=' ')
