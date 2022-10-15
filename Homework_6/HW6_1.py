# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def fact (n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


fact_lamb=lambda n: 1 if n==1 else n*fact_lamb(n-1)  #добавлено


num = input('Введите натуральное число больше 0: ')
while not (num[0] !='0' and num.isdigit()):
    num = input('Введите натуральное число больше 0: ')
num=int(num)

n_list=[f'n={i}' for i in range(1,num+1)]

fact_list=[fact(n) for n in range(1, num+1)]

fact_list_1=[fact_lamb(n) for n in range(1, num+1)]

print(list(zip(n_list, fact_list, fact_list_1)))
