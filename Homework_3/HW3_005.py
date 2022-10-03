# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def user_input():
    num = input('Введите число: ')
    while not num.isdigit():
        num = input('Введите число: ')
    return int(num)

num = user_input()
if num==0:
    print ([0])
elif num==1:
    print ([1,0,1])
else:
    n1,n2=1,1
    fib=[-1,1,0,1,1]
    for i in range(2,num):
        fn=n1+n2
        fib.insert(-i*4,(-1)**i*fn) #отрицательная часть
        fib.append(fn)  #положительная часть
        n1,n2=n2,fn 
    print (fib)