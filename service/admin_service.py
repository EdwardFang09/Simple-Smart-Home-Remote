import mysql.connector




def login_to_db(user, password, new_password, notification):
    db = mysql.connector.connect(host="localhost",
                                 user='IEE',
                                 password='IEE',
                                 db="sora_smart_home")

    cursor = db.cursor()

    cursor.execute('''select * from users_pw''')
    my_result = cursor.fetchall()

    ad_password = my_result[0][1]
    pr_password = my_result[0][2]
    cd_password = my_result[0][3]
    gs_password = my_result[0][4]

    if user == 'admin' and password == ad_password:
        dispatch(user, new_password, notification)

    elif user == 'parent' and password == pr_password:
        dispatch(user, new_password, notification)

    elif user == 'guest' and password == gs_password:
        dispatch(user, new_password, notification)

    elif user == 'child' and password == cd_password:
        dispatch(user, new_password, notification)

    elif user == '' or password == '' or new_password == '':
        dispatch(user, new_password, notification)

    else:
        text = "Username or password is incorrect!"
        print(text)
        notification.config(text=text)
        notification.place(x=90, y=50)


def dispatch(user, new_password, notification):
    db = mysql.connector.connect(host="localhost",
                                 user='IEE',
                                 password='IEE',
                                 db="sora_smart_home")

    cursor = db.cursor()

    cursor.execute(f'''UPDATE users_pw SET {user} = '{new_password}' where id = 1''')
    text = f'{user} password changed successfully to "{new_password}"!'
    print(f'Email to {user}: {text}')
    notification.config(text=text)
    notification.place(x=50, y=50)
    db.commit()
