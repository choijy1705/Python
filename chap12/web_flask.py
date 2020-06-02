# Flask : 웹 어플리케이션을 개발하는 데 필요한 마이크로 웹 프레임워크
# 설치방법(anaconda prompt)
# - conda install Flask(가상 환경에서 설치) * 가상환경(tf_cpu) - 원본환경에는 전혀 영향을 끼치지 않도록 한다.

# 플라스크를 임포트 합니다.
from flask import Flask
from flask import request

# 플라스크 앱을 생성.
app = Flask(__name__)

# 편의를 위한 디버그 모드를 활성화합니다.
app.debug = True

# URL 경로에 따라 실행할 함수에 데코레이터를 사용합니다.
# 데코레이터의 파라메터는 URL 경로입니다.
@app.route("/")
def hello(): # 위 경로에 접근하면 실행 할 함수 등록
    return "Hello World!!!"

@app.route("/hello/<name>") # <name> 자리에 오는 문자열은 name에 할당되어 함수로 전달합니다.
def hello_to(name):
    return 'Hello, {0}'.format(name)

@app.route("/hello")
def hello_to_get_param():
    # /hello?name=kang와 같은 형식의 요청을 받아서
    # ?name=<이름>의 값이 오면, <이름>을 name에 저장합니다.
    name = request.args.get("name")
    return "Hello, {0}!".format(name)

# 이 파일은 바로 실행할 때 함께 실행할 코드를 작성한다.

if __name__ == "__main__":
    app.run() # 위에서 생성한 플라스크 애플리케이션을 실행합니다.