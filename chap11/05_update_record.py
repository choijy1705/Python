import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
update phonebook set phone=?, email=? where name=?''',('070-1234-5678','abcd@xyz.com','박명수'))

conn.commit() # 변경 내용이 있을 때는 commit을 실행해줘야한다.

cursor.close()
conn.close()
