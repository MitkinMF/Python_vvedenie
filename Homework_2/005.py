#  Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0,1,2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5,1,8]

import random
n=10
spisok = [item for item in range(0, n)]

print(spisok)

for i in range(len(spisok)):
    j=random.randint(0,len(spisok)-1)
    temp=spisok[i]   
    spisok[i]=spisok[j]
    spisok[j]=temp
    
print(spisok)
