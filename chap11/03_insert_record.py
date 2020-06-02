import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
insert into phonebook(name, phone, email) values(?,?,?)
''', ('강호동','010-1111-1111','hodong@company.com'))
cursor.execute('''
insert into phonebook(name, phone, email) values(?,?,?)
''', ('박명수','010-2222-2222','myoungsoo@park.com'))

id = cursor.lastrowid # 마지막 레코드의 index를 반환해준다.
print(id)
conn.commit()

cursor.close()
conn.close()