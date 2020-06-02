class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod # java에서는 static, class method 같은 거지만 python에서는 구분해주고 있다. 기능은 똑같다.
    def print_instance_count(cls): # class method일때는 cls라는 매개변수를 정의 해줘야한다.
        print(cls.count)

if __name__ == '__main__':
    a = InstanceCounter()
    InstanceCounter.print_instance_count()

    b = InstanceCounter()
    InstanceCounter.print_instance_count()

    c = InstanceCounter()
    c.print_instance_count()

    InstanceCounter.count = 10
    InstanceCounter.print_instance_count()
    # 정보은닉은 객체지향이 추구하는 기본 컨셈