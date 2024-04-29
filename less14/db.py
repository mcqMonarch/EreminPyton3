import fnmatch
import hashlib

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

    def add_user(self, login, password, rt_password ,email):
        if fnmatch.fnmatch(email, '*?@*?.*?'):
            if email not in self.select_all_email():
                def check_correct_password():
                    return all([password == rt_password, len(password) >= 8])

                if check_correct_password():
                    request = (f"INSERT INTO users (login, password, email) "
                               f"VALUES ('{login}', '{hashlib.sha3_256(password.encode("utf8")).hexdigest()}', '{email}')")
                    with self.connect.cursor() as c:
                        c.execute(request)
                        self.connect.commit()
                        return True
                else:
                    print('Проверьте пароль')
            else:
                print('Email уже используется')
        else:
            print('Проверьте написание email')

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
    bd.add_user('Detyainterneta', '00000000', '00000000',  'Detinterneta@gmail.com')
