class Calculator:

    @staticmethod  # static method 인스턴스를 생성하기전에 메모리에 할당된다. static 변수와 동작이 똑같다.
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a,b):
        return a * b

    @staticmethod
    def divide(a,b):
        return a / b

if __name__ == '__main__':
    print('{0} + {1} = {2}'.format(7, 4, Calculator.plus(7,4)))
    print('{0} - {1} = {2}'.format(7, 4, Calculator.minus(7, 4)))
    print('{0} * {1} = {2}'.format(7, 4, Calculator.multiply(7, 4)))
    print('{0} / {1} = {2}'.format(7, 4, Calculator.divide(7, 4)))