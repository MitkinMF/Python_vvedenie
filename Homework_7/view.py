
def read_file(frmt:str):
    if frmt=='1':
        with open('tel_book.csv', 'r', encoding='utf-8') as f:
            tb=[tuple(my_str.rstrip('\n').split(';')) for my_str in f if my_str !='\n']
        print('Справочник tel_book.csv загружен')
        return tb
    elif frmt=='2':   
        with open('tel_book.txt', 'r', encoding='utf-8') as f:
            tmp=[my_str.rstrip('\n').split()[0] for my_str in f if my_str !='\n']
            tb=[(tmp[0+i*3], tmp[1+i*3],tmp[2+i*3]) for i in range (int(len(tmp)/3))]
        print('Справочник tel_book.csv загружен')
        return tb
    
def out_to_screen(my_list:list):
    print('Фамилия  |   Имя   |  Телефон')
    print('_____________________________________________')
    for elem in my_list:
        print(f'{elem[0]}  |  {elem[1]}  |  {elem[2]}')   
        
         
def out_to_bot(my_list:list):
    s= 'Фамилия  |   Имя   |  Телефон \n _____________________________________________ \n'
    for elem in my_list:
        s += f'{elem[0]}  |  {elem[1]}  |  {elem[2]} \n' 
    return s

def person_input():
    n_p=input('Введите запись в формате: Фамилия Имя Телефон\n')
    new_pers=tuple(n_p.rstrip('\n').split())
    return new_pers
    
def cmd_input():
    return input('Введите команду: ')    

def main_menu():
    print ('''Главное меню:
1 - Чтение файла
2 - Добавление записи
3 - Вывод справочника на экран 
4 - Вывод справочника в файл
0 - Выход''')
     
def menu_select_out_format():
    print ('''Выбор формата записи:
1 - .csv
2 - .txt''')

def menu_select_read_file():
    print ('''Выбор файла для чтения:
1 - tel_book.csv
2 - tel_book.txt''')


def out_file(my_list:list, frmt:str):
    if frmt=='1':
        with open('tel_book.csv', 'w', encoding='utf-8') as file:
            for elem in my_list:
                file.write(f'{elem[0]};{elem[1]};{elem[2]}\n')
            print('Справочник сохранен в файле tel_book.csv')
        return    
    elif frmt=='2':
        with open('tel_book.txt', 'w', encoding='utf-8') as file:
            for elem in my_list:
                file.write(f'{elem[0]}\n{elem[1]}\n{elem[2]}\n')
            print('Справочник сохранен в файле tel_book.txt')
        return      
         

