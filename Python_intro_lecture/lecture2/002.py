with open('file.txt', 'w') as data:
     data.write('line 1\n')
     data.write('line 2\n') # в этой  конструкции close не надо дописывать

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # a-открытие для добавления в конец файла, r-открытие для чтения, w – открытие для записи данных (перезаписывается)
data.writelines(colors) # разделителей не будет
data.close() #закрытие

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()