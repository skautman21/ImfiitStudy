import sqlite3

conn = sqlite3.connect('ids_users_vk.db')
cursor = conn.cursor()


def rebuild():
    cursor.execute("DROP TABLE ids")
    cursor.execute('''CREATE TABLE ids (id INTEGER, is_admin TINYINT(1) DEFAULT 0);''')
    cursor.execute('''CREATE UNIQUE INDEX id_from_user ON ids(id);''')
    cursor.execute('''INSERT INTO ids VALUES (173760002, 1)''')
    cursor.execute('''INSERT INTO ids VALUES (59646831, 1)''')
    conn.commit()


def get_sql(msg):
    a = cursor.execute(f'''{msg}''')
    return (cursor.fetchall())


def check_id(id):
    # a = cursor.execute(f'''SELECT COUNT(*) FROM ids WHERE id={id}''')
    # a = cursor.fetchall()[0][0]
    a = get_sql(f'SELECT COUNT(*) FROM ids WHERE id={id}')[0][0]
    return (a > 0)


def vnosim_id(id):
    #
    # result = cursor.execute("SELECT COUNT(*) FROM ids WHERE")
    cursor.execute(f'''REPLACE INTO ids (id) VALUES ('{id}')''')
    conn.commit()
    rows = get_sql('SELECT * FROM ids')
    print(rows)

def check_is_admin(id):
    a = get_sql(f'SELECT * FROM ids WHERE id={id}')[0][1]
    return (a==1)

