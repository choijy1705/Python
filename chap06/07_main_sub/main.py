
import sub  # sub에 있는 파일을 가져오겠다는 뜻


# sub에서 실행하면 __main__을 피드백해준다. __name__ 을 실행하면 __main__을 피드백해주지만 import를 통해서 실행되면 import된 파일의 이름을 피드백해준다.

print("beginning of main.py...")
print('name:{0}'.format(__name__))
print("end of main.py...")