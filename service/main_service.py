import mysql.connector
import tkinter as tk


def write(location, object_name, status):
    db = mysql.connector.connect(host="localhost",
                                 user='IEE',
                                 password='IEE',
                                 db="sora_smart_home")

    cursor = db.cursor()
    cursor.execute(f'''UPDATE {location} SET {object_name} = {status}''')

    if status == 1:
        string_status = 'ON'

    else:
        string_status = 'OFF'

    cursor.execute(f'''insert into logger(info) values ('{location} {object_name} is turned {string_status}');''')
    db.commit()


def on_off(results):
    if results == 1:
        return 'ON'

    else:
        return 'OFF'


def read(location, number):
    db = mysql.connector.connect(host="localhost",
                                 user='IEE',
                                 password='IEE',
                                 db="sora_smart_home")

    cursor = db.cursor()

    cursor.execute(f'''
    select * from {location}
    ''')

    my_result = cursor.fetchall()

    for x in my_result:
        return on_off(x[number])


def mode_on_state(a1, switch, location, object_name, on='ON'):
    a1["state"] = tk.NORMAL
    switch["text"] = on
    return write(location, object_name, 1)


def mode_off_state(a1, switch, location, object_name, off='OFF'):
    a1["state"] = tk.DISABLED
    switch["text"] = off
    return write(location, object_name, 0)


def mode_read(location, number, on='ON', off='OFF'):
    status = read(location, number)
    if status == 'ON':
        return on
    else:
        return off


def mode_state(a1, switch, location, number, object_name, on='ON', off='OFF'):
    status = mode_read(location, number, on, off)
    if status == on:
        return mode_on_state(a1, switch, location, object_name, on)

    else:
        return mode_off_state(a1, switch, location, object_name, off)


def mode_convert(a1, switch, location, object_name, on='ON', off='OFF'):
    if a1['state'] == tk.DISABLED:
        return mode_on_state(a1, switch, location, object_name, on)

    elif a1['state'] == tk.NORMAL:
        return mode_off_state(a1, switch, location, object_name, off)


def save_log(location, object_name, status):
    db = mysql.connector.connect(host="localhost",
                                 user='IEE',
                                 password='IEE',
                                 db="sora_smart_home")

    cursor = db.cursor()
    cursor.execute(f'''insert into logger(info) values ('{location} {object_name} is turned {status}');''')
    db.commit()
