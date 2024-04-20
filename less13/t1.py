import sqlite3 as sql


connect = sql.connect('test.db')
c = connect.cursor()
connect.cursor().execute("CREATE TABLE IF NOT EXISTS \'users\' (\'id\' STRING, \'nickname\' STRING)")
nickname = input('Nickname: ')
c.execute(f'INSERT INTO \'users\' (\'id\', \'nickname\') VALUES (\'1\', \'{nickname}\')')
connect.commit()
connect.cursor().close()
c.execute('SELECT * FROM \'users\'')
rows = c.fetchall()
print(rows)
