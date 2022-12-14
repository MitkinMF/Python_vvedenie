import datetime
import time
import logger
import students_func as stf
import subjects_func as suf


def estimates_func_create(e_conn, e_cur):
    exec_str = 'SELECT max(estimates_id)+1 FROM estimates'
    e_cur.execute(exec_str)
    new_id = e_cur.fetchone()[0]+1
    exec_str = 'SELECT subject_id, name FROM subjects'
    e_cur.execute(exec_str)
    list_subjects = e_cur.fetchall()
    for index in range(len(list_subjects)):
        print(f'ID: {list_subjects[index][0]} {list_subjects[index][1]}')
    subject_id = int(
        input(f'Введите ID предмета по которому ставите оценку: '))
    stf.show_student(e_cur)
    student_id = int(input(f'Введите ID ученика, которому ставите оценку: '))
    estimate = int(input(f'Введите оценку ученика: '))
    date = round(time.time() * 1000)
    exec_str = f'INSERT INTO estimates (estimates_id, subject_id, student_id, time, estimate) VALUES ({new_id}, '\
               f'{subject_id}, {student_id}, {date}, {estimate})'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Оценка успешно выставлена')
    logtext = f'Ученику: {student_id} по предмету: {subject_id} выставлена {estimate}'
    logger.exp_txt(logtext)


def estimates_func_delete(e_conn, e_cur):
    exec_str = "select subject_id, name from subjects;"
    suf.show_subjects(e_cur)
    subject_id = int(
        input(f'Введите ID предмета оценку по которому нужно удалить: '))
    stf.show_student(e_cur)
    student_id = int(
        input(f'Введите ID ученика оценку которого нужно удалить: '))
    print('Cписок оценок:')
    show_estimates(e_cur, student_id, subject_id)
    estimates_id = int(input(f'Введите ID оценки которую нужно удалить: '))
    exec_str = f'DELETE from estimates  WHERE estimates_id = {estimates_id}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print('Новый cписок оценок:')
    show_estimates(e_cur, student_id, subject_id)
    logtext = f'Ученику: {student_id} по предмету: {subject_id} удалена оценка {estimates_id}'
    logger.exp_txt(logtext)


def estimates_func_modify(e_conn, e_cur):
    suf.show_subjects(e_cur)
    subject_id = int(
        input(f'Введите ID предмета оценку по которому нужно изменить: '))
    stf.show_student(e_cur)
    student_id = int(
        input(f'Введите ID ученика оценку которого нужно изменить: '))
    print('Список оценок:')
    show_estimates(e_cur, student_id, subject_id)
    estimates_id = int(input(f'Введите ID оценки которую нужно изменить: '))
    estimate = int(input(f'Введите оценку ученика: '))
    date = round(time.time() * 1000)

    exec_str = f'UPDATE estimates set subject_id="{subject_id}", student_id="{student_id}", '\
               f'time="{date}", estimate="{estimate}"  WHERE estimates_id = {estimates_id}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Оценка успешно изменена')
    logtext = f'Ученику: {student_id} по предмету: {subject_id} изменена оценка на {estimate}'
    logger.exp_txt(logtext)


def show_estimates(e_cur, student_id, subject_id):
    exec_str = f'SELECT estimates_id, time, estimate from estimates where (subject_id={subject_id} '\
        f'and student_id={student_id});'
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список оценок:')
    for index in range(len(buf_list)):
        date = str(datetime.datetime.fromtimestamp(
            buf_list[index][1] / 1000.0)).split('.')[0]
        print(f'ID: {buf_list[index][0]}\t{date}\t{buf_list[index][2]}')


def show_estimates_full(e_cur):
    exec_str = f'SELECT student_id, lastname, firstname, patronymic, class, time, name, estimate '\
                f'FROM v_full ORDER BY student_id, name;'
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список учеников с оценками:')
    for index in range(len(buf_list)):
        student_id = buf_list[index][0]
        lastname = buf_list[index][1]
        firstname = buf_list[index][2]
        patronymic = buf_list[index][3]
        cls_number = buf_list[index][4]
        date = str(datetime.datetime.fromtimestamp(buf_list[index][5] / 1000.0)).split('.')[0]
        subj = buf_list[index][6]
        estimate = buf_list[index][7]
        if index > 0 and student_id == buf_list[index-1][0]:
            text = f'\t предмет: {subj} оценка: {estimate} дата: {date}'
            print(text)
            logger.exp_txt(text)
        else:
            text = f'ID: {student_id} ФИО: {lastname} {firstname} {patronymic} класс: {cls_number} \n '\
                    f'\t предмет: {subj} оценка: {estimate} дата: {date}'
            print(text)
            logger.exp_txt(text)
