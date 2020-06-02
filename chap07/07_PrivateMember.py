class HasPrivate:
    def __init__(self): # private 과 public의 구분은 이름으로 구분한다. 외부에서의 접근 권한의 차이가 private과 public의 차이.
        self.public1 = "public1"
        self.__private1 = "private1"
        self.__private2_ = "private2"
        self.__public2__ = "public2"

    def print_from_internal(self):
        print(self.public1)
        print(self.__private1)
        print(self.__private2_)
        print(self.__public2__)


if __name__ == '__main__':
    obj = HasPrivate()
    obj.print_from_internal()

    print("============")

    print(obj.public1)
    # print(obj.__private1) error 발생, private 으로 선언되어 있기 때문에
    # print(obj.__private2_)
    print(obj.__public2__)