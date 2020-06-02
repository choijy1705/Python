
if __name__ == '__main__':
    def my_power(y):
        print("숫자를 입력하세요.")
        x = input()
        return int(x) ** y

    print(my_power(2))

'''
# 파이썬의 예외 처리 구문1
    try:
        # 문제가 없을 경우 실행 할 코드
    except:
        # 문제가 생겼을 때 실행 할 코드
'''


try:
    print(1/0)
except:
    print("예외가 발생했습니다.")

print("프로그램 종료")

'''
# 파이썬의 예외 처리 구문2
    try:
        # 문제가 없을 경우 실행 할 코드
    except: 예외형식1
        # 문제가 생겼을 때 실행 할 코드
    except: 예외형식2
        # 문제가 생겼을 때 실행 할 코드
'''

my_list = [ 1, 2, 3]

try:
    print("첨자(index)를 입력하세요 :")
    index = int(input())
    print(my_list[index] / 0)
except IndexError:
    print("잘못된 첨자입니다.")
except ZeroDivisionError:
    print("0으로 나눌수 없습니다.") # 갯수에 상관없이 예외를 계속 추가할 수 있다.

'''
# 파이썬의 예외 처리 구문3
    try:
        # 문제가 없을 경우 실행 할 코드
    except 예외형식1 as e:
        # 문제가 생겼을 때 실행 할 코드
    except 예외형식2 as e:
        # 문제가 생겼을 때 실행 할 코드
'''
my_list = [ 1, 2, 3]
print("==== as ====")
try:
    print("첨자(index)를 입력하세요 :")
    index = int(input())
    print(my_list[index] / 0)
except IndexError as err:
    print("잘못된 첨자입니다.({0})".format(err))
except ZeroDivisionError as err:
    print("0으로 나눌수 없습니다({0})".format(err)) # 갯수에 상관없이 예외를 계속 추가할 수 있다.

'''
–try절을 무사히 실행하면 만날 수 있는 else
    try:
         # 실행할 코드 블록 
    except: 
         # 예외 처리 코드 블록 
    else: 
         # except절을 만나지 않았을 경우 실행하는 코드 블록
'''
print("===else===")
my_list = [1, 2, 3]

try:
    print("인덱스를 입력하세요")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except:
    print("예외가 발생했습니다.")
else:
    print("리스트의 요소 출력에 성공")
'''
# 반드시 실행되는 finally
    try:
         # 실행할 코드 블록 
    except: 
         # 예외 처리 코드 블록 
    else: 
         # except절을 만나지 않았을 경우 실행하는 코드 블록
    finally:
        # try가 실행되든 except가 실행되는 마지막에 finally가 실행이 되도록 하는 구문(python 의 특이한 구문)
          
    or
    
    try:
         # 실행할 코드 블록 
    except: 
         # 예외 처리 코드 블록 
    finally:
        # try가 실행되든 except가 실행되는 마지막에 finally가 실행이 되도록 하는 구문(python 의 특이한 구문)   
'''

print("===finally===")
my_list = [1, 2, 3]

try:
    print("인덱스를 입력하세요")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except:
    print("예외가 발생했습니다.")
finally:
    print("어떤 일이 있어도 마무리 합니다.")

'''
# Exception 클래스
- 예외 관련 상속의 관계도
    BaseException (최상위 클래스)
        SystemExit
        Keyboardinterrupt
        GeneratorExit
        Exception
            ...
            ArithmeticError
                ZeroDivsionError
                ...

            LookupError
                IndexError
                ...
            ...


'''
# 예외가 발생하면 첫번째 except 부터 보게 되는데 Exception이 zerodivision과 index를 포함하기 때문에 Exception Error 갈 발생하게 된다.
my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요:")
    index = int(input())
    print(my_list[index] / 0)

except ZeroDivisionError as err:
    print("2) 0으로 나눌 수 없습니다.({0})".format(err))
except IndexError as err:
    print("3) 잘못된 인덱스 입력.({0})".format(err))
except Exception as err: # 모든 예외를 처리하기위해서 가장 상위클래스이 예외는 마지막에 두어야 한다.
    print("1) 예외가 발생.({0})".format(err))


# 강제 예외 발생
# ex1)
print("====강제 예외 발생======")
text = input()
if text.isdigit() == False:
    raise Exception("입력 받은 문자열이 숫자로 구성되어 있지 않습니다.")

# ex2)
try:
    raise Exception("예외를 일으킵니다.")
except Exception as e:
    print("예외가 발생하였습니다. : {0}".format(e))

print("프로그램 종료.")

# 사용자 정의 예외
def some_function():
    print("1~10 사이의 수를 입력하세요:")
    num = int(input())

    if num < 1 or num > 10:
        raise Exception("유효하지 않은 숫자입니다.{0}".format(num))
    else:
        print("입력한 수는 {0}입니다.".format(num))
try:
    some_function()
except Exception as err:
    print("예외가 발생했습니다. {0}".format(err))

'''
try:
    # 예외 발생
except:
    raise
'''

def some_function_caller():
    try:
        some_function()
    except Exception as err:
        print("1)예외가 발생했습니다.{0}".format(err))
        raise

try:
    some_function_caller()

except Exception as err:
    print("2)예외가 발생했습니다.{0}".format(err))

# 사용자 정의 예외 형식
'''
class MyException(Exception):
    def __init__(self):
        super().__init__("MyException이 발생했습니다.")

everythis_is_fine = False
if everythis_is_fine == False:
    raise MyException()
'''

class InvalisdIntException(Exception):
    def __init__(self, arg):
        super().__init__('정수가 아닙니다. : {0}'.format(arg))

def conver_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalisdIntException(text)

if __name__ == '__main__':
    try:
        print("숫자를 입력하세요 :")
        text = input()
        number = conver_to_integer(text)
    except InvalisdIntException as err:
        print("예외가 발생했습니다({0})".format(err))
    else:
        print('정수 형식으로 변환되었습니다.{0}({1})'.format(number, type(number)))