# Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x,y,z=0,0,0
solve=not(x or y or z)== (not x) and (not y) and (not z)
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x,y,z, solve)
        
