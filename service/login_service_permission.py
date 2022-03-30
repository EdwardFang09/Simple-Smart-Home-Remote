import mysql.connector
from GUI import RemoteGUIforAdmin as Ra
from GUI import RemoteGUI as Rp

# Order according to MySQL
# admin: 0
# parent: 1
# guest: 2
# child: 3


def read_perm(user):
    db = mysql.connector.connect(host="localhost",
                                 user='IEE',
                                 password='IEE',
                                 db="sora_smart_home")

    cursor = db.cursor()

    cursor.execute('''select * from permission''')
    my_result = cursor.fetchall()

    if user == 'admin':
        number = 0

    elif user == 'parent':
        number = 1

    elif user == 'guest':
        number = 2

    elif user == 'child':
        number = 3

    return perm_action(my_result[0][number], user)

# Type of permissions:
# 4: Admin power, access to Admin GUI only
# 3: Parent power, access to parental tools (remote mode + guest mode)
# 2: Guest power, access to remote if guest mode is on
# 1: Child power, no permissions


def perm_action(permission, user):
    if permission == 4:
        return Ra.run()

    else:
        return Rp.main_run(permission, user)
