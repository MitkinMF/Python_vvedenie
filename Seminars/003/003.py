my_list = ["123", "234", 123 , "567"]
count = 0
user_string = input('Insert your string: ')
for i, elem in enumerate(my_list):
    if user_string in elem:
        count += 1
        if count == 2:
            print(i)
            break
else:
    print('Ее нет')


my_list = ["123", "234", 123 , "567"]

user_string = my_list[0]

if user_string in my_list[1:]:
    print(my_list.index(user_string, 1))
else:
    print(-1)
