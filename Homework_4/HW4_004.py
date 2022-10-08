#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
def create_poly():
    k = input('Введите натуральное число больше 0: ')
    while not (k[0] != '0' and k.isdigit()):  # проверка на число
        k = input('Ошибка. Введите натуральное число больше 0: ')
    k = int(k)
    numbers = [random.randint(0,5) for item in range(0, k+1)] #генератор списка коэффициентов
    s = ''
    for item in numbers: #генератор строки многочлена
        if k>1:
            if item !=0:
                s=s+f'{item}*x^{k} '
                s=s+random.choice('+-')+' '              
        elif k==1:
            if item !=0: 
                s=s+f'{item}*x '
                s=s+random.choice('+-')+' '
        elif k==0:
            if item !=0:
                s=s+f'{item} ' 
            else:
                s=s.rstrip()
                s=s.rstrip(s[-1])
        k-=1
    if 'x' in s:
        s=s+'= 0'
    return s 
path = 'poly.txt'
with open(path, 'w') as data:
    data.writelines(f'{create_poly()}') #запись строки в файл
    data.writelines(f'\n{create_poly()}')
    data.writelines(f'\n{create_poly()}')