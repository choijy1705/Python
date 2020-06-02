import sys

print(sys.builtin_module_names) # 파이썬 인터프리터 내장 모듈, 모듈의 list들을 보여준다.

for path in sys.path:
    print(path)

"""     주석문형식으로 쓰인다.
C:\workspaces\python\chap06 # 파이썬 모듈이 실행되고 있는 현재 디렉토리
C:\workspaces\python\chap06
C:\ProgramData\Anaconda3\envs\tf_cpu\python37.zip # 파이썬 함께 설치된 
C:\ProgramData\Anaconda3\envs\tf_cpu\DLLs
C:\ProgramData\Anaconda3\envs\tf_cpu\lib
C:\ProgramData\Anaconda3\envs\tf_cpu
C:\ProgramData\Anaconda3\envs\tf_cpu\lib\site-packages
C:\ProgramData\Anaconda3\envs\tf_cpu\lib\site-packages\win32
C:\ProgramData\Anaconda3\envs\tf_cpu\lib\site-packages\win32\lib
C:\ProgramData\Anaconda3\envs\tf_cpu\lib\site-packages\Pythonwin
"""