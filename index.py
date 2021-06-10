from flask import Flask, request
from flask_cors import CORS
import json, dbHandler, queryString

app = Flask (__name__)
CORS(app)
 
@app.route('/contents/<int:base_id>')
def getContents(base_id):
    # 장르
    sort = request.args.get('sort')
    sort = queryString.sort()
    
    # 정렬
    order = request.args.get('order')
    order = queryString.order()

    # 검색
    keyword = request.args.get('keyword')
    keyword = queryString.keyword()

    # 페이지당 목록 수
    size = request.args.get('size')
    size = queryString.size()

    # 페이지
    page = request.args.get('page')
    page = queryString.page(size)


    list = dbHandler.getContents(base_id, keyword, sort, order, size, page)
    jsonStr = json.dumps(list, ensure_ascii=False)

    return jsonStr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)