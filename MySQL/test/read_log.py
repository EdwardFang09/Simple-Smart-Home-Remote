import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user='IEE',
                             password='IEE',
                             db='sora_smart_home')

cursor = db.cursor()

cursor.execute('''select * from logger;''')
my_result = cursor.fetchall()

for x in my_result:
    print(x)