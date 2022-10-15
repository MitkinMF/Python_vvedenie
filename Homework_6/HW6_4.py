# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Сжатие

with open('Homework_6/data.txt', 'r') as data:
    my_data=data.readline()
count = 1
my_new_data = []
i=0
for i in range(1, len(my_data)):
    if my_data[i] == my_data[i-1]:
        count += 1
    else:
        my_new_data.append(count)
        my_new_data.append(my_data[i-1])
        count = 1
my_new_data.append(count)
my_new_data.append(my_data[i])
with open('Homework_6/zipdata.txt', 'w') as data:
    data.write(''.join(map(str, my_new_data))) #map

# Распаковка
with open('Homework_6/zipdata.txt', 'r') as data:
    my_data1=data.readline()
print(my_data1)
temp_str=''
my_new_data1=''
for item in my_data1:
    if item.isdigit():
        temp_str+=item      
    else:
        my_new_data1=my_new_data1+(int(temp_str)*item)
        temp_str=''
print(my_new_data1)