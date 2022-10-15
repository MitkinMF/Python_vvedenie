# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def fact (n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


fact_lamb=lambda n: 1 if n==1 else n*fact(n-1) #добавлено


num = input('Введите натуральное число больше 0: ')
while not (num[0] !='0' and num.isdigit()):
    num = input('Введите натуральное число больше 0: ')
    
fact_list=list()
fact_list_1=list()

for n in range(1, int(num)+1):
    fact_list.append(fact(n))
    fact_list_1.append(fact_lamb(n))
print (fact_list)
print (fact_list_1)