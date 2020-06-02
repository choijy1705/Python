import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("select * from phonebook") # python은 select 문도 execute를 사용한다.

rows = cursor.fetchall()

for row in rows:
    print("name:{0}, phone:{1}, email:{2}".format(row[0],row[1],row[2])) # R만 index 1부터 카운트 나머지는 모두 0부터 카운트한다.


cursor.close()
conn.close()