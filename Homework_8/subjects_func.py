import logger


def subjects_func_create(e_conn, e_cur):
    exec_str = 'SELECT max(subject_id)+1 FROM subjects'
    e_cur.execute(exec_str)
    new_id=e_cur.fetchone()[0]+1
    subject_name = input('Введите название предмета: ')
    exec_str = f'INSERT INTO subjects (subject_id, name) VALUES ({new_id}, ' \
               f'"{subject_name}")'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Предмет: {subject_name} успешно добавлен')
    logtext = f'Предмет: {subject_name} успешно добавлен'
    logger.exp_txt(logtext)


def subjects_func_delete(e_conn, e_cur):
    exec_str = 'SELECT max(subject_id) FROM subjects'
    show_subjects(e_conn, e_cur)
    number = int(input(f'Введите ID предмета, который вы хотели бы удалить: '))
    exec_str = f'DELETE from subjects  WHERE subject_id = {number}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Предмет с ID: {number} удален из базы')
    show_subjects(e_conn, e_cur, 'Новый список предметов:')
    logtext = f'Предмет с ID: {number} удален из базы'
    logger.exp_txt(logtext)


def subjects_func_modify(e_conn, e_cur):
    exec_str = 'SELECT max(subject_id) FROM subjects'
    show_subjects(e_conn, e_cur)
    number = int(input(f'Введите ID предмета, который вы хотели бы изменить: '))
    subject_name = input('Введите название предмета: ')
    exec_str = f'UPDATE subjects set name="{subject_name}" WHERE subject_id = {number}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Предмет с ID: {number} был изменен в базе')
    show_subjects(e_conn, e_cur, 'Новый список предметов:')
    logtext = f'Предмет с ID: {number} был изменен в базе'
    logger.exp_txt(logtext)


def show_subjects(e_cur):
    exec_str = "select subject_id, name from subjects;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список предметов:')
    for index in range(len(buf_list)):
        print(f'{buf_list[index][0]}\t{buf_list[index][1]}')
        logtext = f'{buf_list[index][0]}\t{buf_list[index][1]}'
        logger.exp_txt(logtext)
