# file에 write 하기.

file = open('text.txt', 'w') # 연결하고자 하는 파일을 패스와 함께 적기
file.write('hello')
file.close()

# file에서 데이터 읽어오기

file = open('text.txt', 'r') # mode 생략(default : 'rt')
str = file.read()
print(str)
file.close()