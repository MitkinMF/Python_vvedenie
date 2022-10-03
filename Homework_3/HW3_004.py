def user_input():
    num = input('Введите число: ')
    while not num.isdigit():
        num = input('Введите число: ')
    return int(num)

print(f'{user_input():b}')