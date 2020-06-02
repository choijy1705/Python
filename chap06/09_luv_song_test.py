import sub_luv_song.call_module01
import sub_luv_song.call_module02

import luv_song.module01 as mod01
import luv_song.module02 as mod02

if __name__ == '__main__':
    print("===main===")   # 코드 오동작이나 잘못된곳에서 실행되는 문제점을 조건을 이용하여 해결할 수 있다.
    mod01.test()
    mod02.test()