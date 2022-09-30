# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact (n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

num = input('Введите натуральное число больше 0: ')
while not (num[0] !='0' and num.isdigit()):
    num = input('Введите натуральное число больше 0: ')
    
fact_list=list()
for n in range(1, int(num)+1):
    fact_list.append(fact(n))
print (fact_list)