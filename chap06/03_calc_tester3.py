from my_package.calculator import *  # package안에 포함된 모든 함수들을 import시킬 수 있다. import한 함수(변수)의 불명확성, 가독성이 떨어짐. 비권장
# 안에 정의 되어 있는 모든 모듈이 포함되기 때문에 실제 사용되지 않는 파일들도 import되어 파일 사이즈가 커지는 단점이 있다.

print(plus(10,5))
print(minus(10,5))