#  Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0,1,2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5,1,8]

import random
n=10
spisok = [random.randint(0,n) for item in range(0, n)]

print(spisok)

for i in range(len(spisok)):
    j=random.randint(0,len(spisok)-1)
    temp=spisok[i]   
    spisok[i]=spisok[j]
    spisok[j]=temp
    
print(spisok)



list = [1, 2, 3, 4, 5, 6]
for i in range(len(list)):
    a =  random.randint(0,len(list) -1)
    if list[i] != list[a]:
        list[i],list[a] = list[a],list[i] #перестановка
        print(list[i], list[a])
print(list)


my_list = [1, 2, 3, 4, 5, 6]
for i, elem in enumerate(my_list):
    a =  random.randint(0,len(my_list) -1)
    if elem != my_list[a]:
        elem,my_list[a] = my_list[a],elem
        print(elem, my_list[a])
print(my_list)
