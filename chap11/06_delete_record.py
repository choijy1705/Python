import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
delete from phonebook where email = ?
''',('abcd@xyz.com',)) # 자료형이 튜플이기 때문에  자료형의 구분을 위하여 하나일때는 반드시 튜플인지 아닌지를 구분해주기 위하여 , 가 들어가야한다.

conn.commit()

cursor.close()
conn.close()
