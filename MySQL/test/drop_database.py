import mysql.connector

mysql_password = input('Insert MySQL root password: ')
db = mysql.connector.connect(host="localhost",
                             user='root',
                             password=mysql_password,
                             db='mysql')

cursor = db.cursor()

cursor.execute('''drop database sora_smart_home;''')