class ClassVar: # 자료형을 구성할때 필드, 생성자 메서드는 필수 구성요소가 아니다.
    text_list = []   # 클래스 멤버
    # * java 에서 static 으로 선언된 변수는 참조변수 선언에 의해 메모리 할당이 되는 것이 아니라 만나자마자 메모리에 할당된다. class 이름으로 접근할 수 있다.
    # 이러한 것을 class 변수라고 불렀다
    # python 에서는 이러한 형태를 만나면 먼저 메모리에 할당한다. java의 static과 똑같은 동작.

    def add(self, text):  # 인스턴스 멤버
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list) # 미리 정의 되어 있기 때문에 얼마든지 꺼내 쓸 수 있다.

if __name__ == '__main__':
    a = ClassVar()
    a.add('a')
    a.print_list() # ['a']

    b = ClassVar()
    b.add('b')
    b.print_list() # ['a', 'b']  변수를 공유한다.


