# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Сжатие
with open('data.txt', 'r') as data:
    my_data=data.readline()
count = 1
my_new_data = []
i=0
for i in range(1, len(my_data)):
    if my_data[i-1] == my_data[i]:
        count += 1
    else:
        my_new_data.append(count)
        my_new_data.append(my_data[i-1])
        count = 1
my_new_data.append(count)
my_new_data.append(my_data[i])
with open('zipdata.txt', 'w') as data:
    data.write(''.join(map(str, my_new_data)))

# Распаковка
with open('zipdata.txt', 'r') as data:
    my_data1=data.readline()
print(my_data1)
temp_str=''
my_new_data1=''
for i in range(0, len(my_data1)):
    if my_data1[i].isdigit():
        temp_str+=my_data1[i]  
        if len(my_data1)==1:
            my_new_data1=my_data1[i]
    else:
        my_new_data1=my_new_data1+(int(temp_str)*my_data1[i])
        temp_str=''
print(my_new_data1)