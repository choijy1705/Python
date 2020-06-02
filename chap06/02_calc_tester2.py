#from my_package.calculator import plus
#from my_package.calculator import minus
from my_package.calculator import plus, minus # 따로 정의 하지 않고 ','를 이용하여 한번에 등록할 수 도 있다.

#from my_package.calculator import multiply
#from my_package.calculator import divide

print(plus(10,5))
print(minus(10,5))
#print(multiply(10,5))
#print(divide(10,5)) # my_package.calculator 모듈의 multiply() 함수를 import하지 않아 현재 모듈에서 보이지 않는 함수

