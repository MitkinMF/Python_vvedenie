path = '1.txt'
path1 = '2.txt'
data = open(path, 'r')
text=[]
for line in data:
    text.append(line.rstrip('\n'))
data.close()
del text[::2]
#print(text)
with open(path1, "w") as data1:
    data1.writelines("%s\n" % line for line in text)