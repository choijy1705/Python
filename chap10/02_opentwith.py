
# file = open('test.txt', 'w')
with open('test.txt','a+t') as file:
    file.write('hello')

with open('test.txt','a+t') as file:
    file.write('python')

with open('test.txt', 'r+t') as file:
    str = file.read()
    print(str)
    # file.close()


'''
# 텍스트 파일 읽기 / 쓰기
    1. 문자열을 담은 리스트를 파일에 쓰는 writelines() 메서드

'''
# ex1)
lines = ["we'll find a way we always have - Interstellar\n",
         "I'll find you and I'll kill you - Taken\n",
         "I'll be back - Terminator 2\n"]

with open('movie_qutoes.txt', 'w') as file:
    file.writelines(lines) # 줄단위로 write한다.

'''
# 텍스트 파일 읽기 / 쓰기
    2. 줄 단위로 텍스트를 읽는 readline() & readlines() 메서드드
'''

# ex1)
with open('movie_qutoes.txt','r') as file:
    line = file.readline() # 라인 단위로 읽어오는 메서드 \n을 만나기 전까지의 한 라인의 문장을 읽어온다.
    # 한 라인을 읽어올때 \n 의 기호까지 읽어오기 때문에 print를 만나면 \n에 의하여 줄바꿈을 하고 print 자체가 줄바꿈을 하기때문에 한칸의 빈여백이 발생하게 된다.
    while line != '': # 빈 문자열을 만나기 전까지 출력을 반복한다.
        print(line)
        line = file.readline()

# ex2)
with open('movie_qutoes.txt','r') as file:
    lines = file.readlines() # 별도의 반복문을 쓸 필요 없다.  처음부터 끝까지 모든 라인을 읽어온다.
    line = ''
    for line in lines:
        print(line, end = '')