import mysql.connector
from GUI import LoginPageGUI as Lg
import sys

sys.setrecursionlimit(10**6)
database_name = 'sora_smart_home'
username = 'IEE'
password = 'IEE'
mysql_password = input("Insert MySQL root password: ")


def login_to_db():
    db = mysql.connector.connect(host="localhost",
                                 user=username,
                                 password=password,
                                 db=database_name)

    cursor = db.cursor()

    cursor.execute('''select * from users_pw''')
    my_result = cursor.fetchall()
    return my_result

def check_user():
    db = mysql.connector.connect(host="localhost",
                                 user='root',
                                 password = mysql_password,
                                 db='mysql')

    cursor = db.cursor()
    print('Loading...')
    cursor.execute('''
    select user from user;
    ''')

    my_result = cursor.fetchall()
    table_length = len(my_result)

    for x in range(0, table_length):
        if my_result[x][0] == username:
            print('Loading user...')
            return check_database()

        elif x == table_length-1:
            print(f"User '{username}' not found!\nCreating user '{username}'...")
            return create_user()


def create_user():
    db = mysql.connector.connect(host="localhost",
                                 user='root',
                                 password = mysql_password,
                                 db='mysql')

    cursor = db.cursor()
    cursor.execute(f'''create user '{username}'@'localhost' identified by '{password}';
    GRANT ALL PRIVILEGES ON * . * TO '{username}'@'localhost';
    FLUSH PRIVILEGES;
    ''')

    print(f"Installing '{database_name}' database...")
    return create_database()


def check_database():
    dbs = mysql.connector.connect(host="localhost",
                                  user=username,
                                  password=password)

    cursors = dbs.cursor()

    cursors.execute('''
        show databases;
        ''')

    my_result = cursors.fetchall()
    table_length = len(my_result)

    for x in range(0, table_length):
        if my_result[x][0] == database_name:
            print(f'Checking {database_name}...')
            return content_check(database_name)

        elif x == table_length-1:
            print(f"Database '{database_name}' not found!\nInstalling database {database_name}...")
            return create_database()


def content_check(database):
    dbs = mysql.connector.connect(host="localhost",
                                  user=username,
                                  password=password,
                                  db=database)

    cursors = dbs.cursor()
    cursors.execute('''show tables;''')
    my_result = cursors.fetchall()
    table_length = len(my_result)

    for x in range(0, table_length):
        if my_result[x][0] == 'trademark':
            cursors.execute('''select * from trademark;''')
            my_result = cursors.fetchall()
            table_length = len(my_result)

            for j in range(0, table_length):
                if my_result[j][0] == 'Made with love':
                    print('Initializing...!')
                    return Lg.start()

                elif j == table_length - 1:
                    print(f"Database '{database}' is either broken or incorrect. Fixing...")
                    return create_database()

        elif x == table_length - 1:
            print(f"Database '{database}' is either broken or incorrect. Fixing...")
            return create_database()


def create_database():
    dbs = mysql.connector.connect(host="localhost",
                                  user=username,
                                  password=password)

    cursors = dbs.cursor(buffered=True)

    file = open('MySQL/script.sql')
    sql = file.read()

    for _ in cursors.execute(sql, multi=True):
        pass

    dbs.commit()

    print('Restarting...')
    return check_user()
