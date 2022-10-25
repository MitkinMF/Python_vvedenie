from os import system
import telephone_book as tb
import view
t_book=[]


def main_loop():
    system("cls")
    global t_book
    flag=1
    while flag:
        view.main_menu()
        s=view.cmd_input()
        if s=='1':
            view.menu_select_read_file()
            t_book=view.read_file(view.cmd_input())           
        elif s=='2':
            tb.person_create(t_book, view.person_input())             
        elif s=='3':
            view.out_to_screen(t_book)
        elif s=='4':  
            view.menu_select_out_format()
            view.out_file(t_book,view.cmd_input())
        elif s=='0':  
            flag=0
            break
        s=input('Нажмите Enter чтобы продолжить')
        system("cls")
        
         
   