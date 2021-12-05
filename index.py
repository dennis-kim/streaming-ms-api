from flask import Flask, request
from flask_cors import CORS
import json, dbHandler, queryString

app = Flask (__name__)
CORS(app)
 
@app.route('/contents/<int:base_id>')
def getContents(base_id):

    # 시리즈 번호
    getSeries = queryString.series(request.args.get('series'))

    # 정렬 타입
    getSort = queryString.sort(request.args.get('sort'))
    
    # 정렬 순서
    getOrder = queryString.order(request.args.get('order'))

    # 검색
    getKeyword = queryString.keyword(request.args.get('keyword'))

    # 페이지당 목록 수
    getSize = queryString.size(request.args.get('size'))

    # 페이지
    getPage = queryString.page(request.args.get('page'), getSize)

    # 결과 취합
    list = dbHandler.getContents(base_id, getSeries, getKeyword, getSort, getOrder, getSize, getPage)
    jsonStr = json.dumps(list, ensure_ascii=False, default=str)

    return jsonStr

@app.route('/genres/<int:base_id>')
def getGenres(base_id):
    list = []
    if(base_id > 0):
        list = dbHandler.getGenres(base_id)

    jsonStr = json.dumps(list, ensure_ascii=False, default=str)
    return jsonStr

@app.route('/series/<int:base_id>')
def getSeries(base_id):
    list = []
    if(base_id > 0):
        list = dbHandler.getSeries(base_id)

    jsonStr = json.dumps(list, ensure_ascii=False, default=str)
    return jsonStr

@app.route('/comments', methods=['GET'])
def getComments():
    # 페이지당 목록 수
    size = request.args.get('size')
    size = queryString.size()

    # 페이지
    page = request.args.get('page')
    page = queryString.page(size)

    list = dbHandler.getComments(size, page)
    jsonStr = json.dumps(list, ensure_ascii=False)

    return jsonStr


@app.route('/comments', methods=['POST'])
def postComments():
    params = request.get_json('comment')
    comment = '"' + params['comment'] + '"'

    list = dbHandler.postComments(comment)

    return '고만 쳐 씨부려'



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)