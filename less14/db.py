import pymysql


class MySQL:

    def __init__(self):
        host = "127.0.0.1"
        port = 3306
        user = 'root'
        password = 'mysql'
        db_name = 'site_users'

        self.connect = pymysql.connect(host=host,
                                       port=port,
                                       user=user,
                                       password=password,
                                       database=db_name)

    def add_user(self, login, password, email):
        if email not in self.select_all_email():
            request = (f"INSERT INTO users (login, password, email) "
                       f"VALUES ('{login}', '{password}', '{email}')")
            # ПРОВЕРКА ПОЧТЫ
            # request = "INSERT INTO users (login, password, email) VALUES ?,?,?"
            with self.connect.cursor() as c:
                c.execute(request,(login, password, email))
                self.connect.commit()
        else:
            print('Email уже используется')

    def select_all(self):
        request = 'SELECT * FROM users'
        with self.connect.cursor() as c:
            c.execute(request)
            rows = c.fetchall()
            return rows

    def select_all_email(self):
        request = 'SELECT email FROM users'
        with self.connect.cursor() as c:
            c.execute(request)
            rows = c.fetchall()
            return [i[0] for i in rows]


if __name__ == '__main__':
    bd = MySQL()
    bd.add_user('detyainterneta', '000000', 'Detyainterneta@gmail.com')
