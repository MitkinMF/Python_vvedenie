# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N
path = 'simple_num.txt' #список простых чисел
data = open(path, 'r')
simplenum_list = []
for line in data:
    simplenum_list.append(line.rstrip('\n'))
data.close()

num = input('Введите натуральное число больше 0: ')
while not (num[0] != '0' and num.isdigit()): # проверка на число
    num = input('Введите натуральное число больше 0: ')

num = int(num)
if num>=(int(simplenum_list[-1]))**2: #проверка на размер числа
    print('Число слишком большое')
else:    
    simple_div=[]
    for simple_num in simplenum_list: #цикл вычисления простых делителей
        if (num % int(simple_num) == 0):
            simple_div.append(simple_num)
            if num == 1:
                break
    print(simple_div)    
