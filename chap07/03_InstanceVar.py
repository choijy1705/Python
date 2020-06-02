class InstanceVar: # 자료형을 구성할때 필드, 생성자 메서드는 필수 구성요소가 아니다.

    def __init__(self):
        self.text_list = []    # 인스턴스 멤버 변수

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == '__main__':
    a = InstanceVar()
    a.add('a')
    a.print_list() # ['a']

    b = InstanceVar()
    b.add('b')
    b.print_list() # ['b']