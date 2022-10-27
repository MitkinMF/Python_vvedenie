import students_func as stf
import subjects_func as suf
import estimates_func as esf
import logger
import view


def main_loop(conn, curs):
    num = -1
    while num != 0:
        view.main_menu()
        num = int(input('Выберете команду (0 - Выход): '))
        if num == 11:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.students_func_create(conn, curs)
        elif num == 12:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.students_func_modify(conn, curs)
        elif num == 13:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.students_func_delete(conn, curs)
        elif num == 21:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.estimates_func_create(conn, curs)
        elif num == 22:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.estimates_func_modify(conn, curs)
        elif num == 23:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.estimates_func_delete(conn, curs)
        elif num == 31:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.subjects_func_create(conn, curs)
        elif num == 32:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.subjects_func_modify(conn, curs)
        elif num == 33:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.subjects_func_delete(conn, curs)
        elif num == 41:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.show_student(curs)
        elif num == 42:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.show_subjects(curs)
        elif num == 43:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.show_estimates_full(curs)
        else:
            if num:
                print('Такой команды нет')
        if num != 0:
            s=input('Для продолжения нажмите Enter')
        logger.exp_txt(f'Была выбрана команда: {num}')
