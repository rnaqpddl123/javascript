''''
index.html -> 버튼 클릭하면 ES의 결과값을 받아서 화면에 table을 동적으로 생성

소스의 실행 구조
- 비동기
app.py -> index.html -> 버튼클릭 ->app.py ->dao.py 의 bank_get2() 결과값을 리턴받아서 app.py -> index.html
'''

from flask.json import jsonify
from flask import Flask, render_template, request
from dao import bank_get2


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index_view():


    return render_template('index.html')

@app.route('/dataget', methods=["get"])
def req_res():
    
    # data = bank_get2()
    # print(data)    
    # print(type(data))
    # return bank_get2()
    return bank_get2()



# 유지현씨 작품
# dao.py에서 json화 해서 안보낸후 데이터 처리했을떄
# 응답된 데이터 첫번째 형식
# js에서 문제 발생
# json 포멧으로 변환하려는 두가지 방식 다 실패
# JSON.parse(문자열) : key와 value의 구조는 큰 따옴표 표기 필수 -> JSON 객체로 변환
# eval("("+문자열+")") -> JSON객체로 변환

# @app.route('/dataget', methods=["get"])
# def req_res():    
#     data = bank_get2()
#     str_data=""
#     for i in range(data):
#         str_data += str(data[i])+","
#     return str_data


if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")