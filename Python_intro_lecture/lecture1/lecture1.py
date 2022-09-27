"""
value=None
a =1123
b= 1.23
print(type (a))
print(type(b))
value = 12367
print(type(value))
s="hello 'world"
print(s)
s='hello "world'
print(s)
print (a,'-', b,'-',s)
print('{} - {} - {}'.format(a,b,s))  #формат по шаблону
print('{1} - {2} - {0}'.format(a,b,s))  #формат по шаблону 
print(f'{a} - {b} - {s}') #интерполяция по шаблону 
f = False
print(f) 
list=['1','2','3',]
col=['hello',1,2,4.5,True]
print(list)
print(col)

print ('введите а')
a=int(input()) # строгое приведение к типу int
print('введите b')
b=int(input())
print(a, '+',b, '=', a+b )

print ('введите а')
a=float(input()) # строгое приведение типа
print('введите b')
b=float(input())
print(a, '+',b, '=', a+b )

a =+123 # унарный плюс
b=-465 #унарный минус

a=2
b=5

c=a-b
print(c)
c=a/b
print(c)
c=a//b #деление в целых числах
print(c)
c=a%b # остаток от деления
print(c)
c = a ** b #возведение в степень
print(c) 

a=1.354556
b=5
c=round(a*b, 5) #округление до пяти знаков после запятой
print(c) 
a=3
a+=5
print(a)

#логические
a=1<4 and 5>2
print(a)
a=1==2
print(a)
a=1!=2
print(a)
a="qwe"
b="qwe"
print(a==b)
a=[1,2]
b=[1,2]
print(a==b)

a=1<3<5<10
print(a)

f= 1>2 or 3<4
print(f)

f= [1,2,3,4]
print (f)
print (2 in f)  # 2 содержится в списке
print (not 2 in f)  

is_odd = not f[0]%2
print(is_odd)


#условия
a = int(input('a = '))
b =int(input('b = '))
if a>b:
    print(a)
else:
    print(b)

a=int(input('a = '))
if a==2:
    print (2)
elif a==3:
    print(3)
elif a==4:
    print(4)
else:
    print(a)            

#циклы
a =23
b= 0
while a !=0:
    b=b * 10 +(a%10)
    a //=10
print(b)    


a =23
b= 0
while a !=0:
    b=b * 10 +(a%10)
    a //=10
else:    
    print("weqwe")
print(b) 


for i in 1,2,3,4,5,6:
    print(i**2)

r = range(10)
for i in r:
    print(i)


for i in range(1,10,2):
    print(i)

for i in 'qwede asdwqr ' :
    print(i)

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
print(text)


numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]


colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

"""
#функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
