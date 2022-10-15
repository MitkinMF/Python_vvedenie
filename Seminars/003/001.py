# 1. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

from time import time

my_random = time()
n = int(input("введите число: "))
print(my_random)
print(my_random % 1)
print(int(my_random % 1 * n))

