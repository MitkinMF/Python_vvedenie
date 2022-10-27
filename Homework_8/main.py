import sqlite3
import controller

conn = sqlite3.connect(f'school.db')
curs = conn.cursor()
controller.main_loop(conn, curs)
curs.close()
conn.close()
