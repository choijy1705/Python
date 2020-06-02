

# 프로그램의 시작 부분만 == 이고 나머지는 !=으로 파일의 시작 부분을 체크할 수 있다.
if __name__ != '__main__':     # sub에서 실행되는 경우 실행이 되지 않도록 구성, 프로젝트의 파일을 보면 이렇게 시작되는 경우를 확인할 수 있다.
    print("beginning of sub.py...")
    print('name:{0}'.format(__name__))  # __main__
    print("end of sub.py...")

# 실행하였을 경우 아무런 값이 나오지 않는다.