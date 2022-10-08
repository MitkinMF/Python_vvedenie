# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

def pars_to_dict(s):  # функция парсинга строки в словарь
    s = s.replace('*x ', '^1 ').replace(' - ', ' -').replace(' + ', ' +')
    s = s.replace(' + ', ' +').replace(' = 0', '').replace('*x', '')
    s_lst = [i for i in s.split()]
    if '^' not in s_lst[-1]:
        s_lst[-1] = s_lst[-1]+'^0'
    s_lst = [list(map(int, (item.split('^')))) for item in s_lst]
    for item in s_lst:
        item.reverse()
    return dict(s_lst)


with open('poly1.txt', 'r') as data:
    x_1 = data.readline()
with open('poly2.txt', 'r') as data:
    x_2 = data.readline()

poly_1 = pars_to_dict(x_1)
poly_2 = pars_to_dict(x_2)
poly_sum = {}

pow_1 = list(poly_1.keys())  # получение списка ключей
pow_2 = list(poly_2.keys())

for i in range(max([list(poly_1.keys())[0], list(poly_2.keys())[0]]), -1, -1):
    if i in pow_1 and i not in pow_2:
        poly_sum[i] = poly_1[i]
    elif i not in pow_1 and i in pow_2:
        poly_sum[i] = poly_2[i]
    elif i in pow_1 and i in pow_2:
        poly_sum[i] = poly_1[i] + poly_2[i]
final = ''
for p, k in poly_sum.items():
    if p > 1:
        if k < 0:
            final += f'{k}*x^{p}'
        else:
            final += f'+{k}*x^{p}'
    elif p == 1:
        if k < 0:
            final += f'{k}*x'
        else:
            final += f'+{k}*x'
    elif p == 0:
        if k < 0:
            final += f'{k} = 0'
        else:
            final += f'+{k} = 0'
if final[0]=='+':
     final=final.lstrip('+')

with open('poly_sum.txt', 'w') as data:
    data.writelines(final)
