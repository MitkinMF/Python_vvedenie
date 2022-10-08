# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

num = input('Введите вещественное число: ')
while not num.lstrip('-').replace('.', '',1).isdigit():
    num = input('Ошибка. Введите вещественное число: ')
acc = input('Введите требуемую точность в формате "0.х1", вместо "х" введите "0" до 9 шт.:')
flag=True
while flag:
    s = ''
    for i in range(10):
        if acc == ('0.'+s+'1'):
            print(round(float(num),(len(acc)-2)))
            flag=False
            break
        else:
            s = s + '0'
    if flag==False:
        break
    else:
        acc = input('Ошибка. Введите требуемую точность в формате "0.х1", вместо "х" введите "0" до 9 шт.:')
   
