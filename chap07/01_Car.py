# new(java에서의 동작) - python에서도 이동작이 적용된다.
#1. 메모리 할당(heap 영역)
#2. self값 반환  * python 에서는 this 대신 self를 이용한다.(self에 주소 저장)
#3. 생성자 호출
#4. return this

class Car: # 참조자료형
    # 생성자
    def __init__(self): # 생성자의 주기능은 field의 초기화, 생성자를 정의, 파이썬에서는 모든 생성자의 정의 이름이 공통적으로 __init__, java보다 직관적
        self.color = 0xFF0000     # python에서는 생성자안에서 field를 정의 하기 때문에 반드시 self를 붙여야한다. self를 생략할 수 없다.
        self.wheel_size = 16      # 바퀴의 크기
        self.dispalcement =  2000 # 엔진 배기량

     # self 는 java의  this 키워드라 생각하면 된다.

    # Method
    def forward(self): # 전진
        pass

    def backward(self): # 후진
        pass

    def turn_left(self): # 좌회전
        pass

    def turn_right(self): # 우회전
        pass

print(dir()) # 클래스 선언과 동시에 생성된 이름공간의 확인(Car)
print(type(Car)) # <class 'type'>

if __name__ == '__main__':
    my_car = Car() # Car 클래스의 객체 my_car 생성, 인스턴스화 했을때 파이썬에서 의미를 가진다. 참조 자료형의 이름에 () 지정해주면 된다. (인스턴스 생성)
    # 생성자 호출형태, Car() class를 찾아가면서 그때 메모리에 할당을 해준다. 별도의 new라는 키워드를 제공해주지 않는다.
    # 데이터를 필요할 때마다 쓰기위하여 메모리에 할당 해준다. java와 마찬가지로 변수를 선언해서 해당 주소값을 담아서 변수를 통하여 해당 객체에 접근한다.

    print('0x{:02X}'.format(my_car.color)) #0x:16진수 표현법 , my_car 멤버변수 접근
            # :02X -> 정수를 2자리의 16진수로 출력하되, 2자리 안되면 빈자리 0으로 채워 출력하라는 의미
    print(my_car.wheel_size)
    print(my_car.dispalcement)

    my_car.forward()   # my_car 멤버 메서드 접근, self라는 키워드는 자료형 선언 안에서만 의미가 있지 밖에서는 의미가 없다.(Method 호출)
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()