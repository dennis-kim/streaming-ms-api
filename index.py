from flask import Flask, request
from flask_cors import CORS
import json, dbHandler

app = Flask (__name__)
CORS(app)
 
@app.route('/contents/<int:base_id>')
def getContents(base_id):
    # 장르
    sort = request.args.get('sort')
    try:
        sort = str.lower(sort)
        if sort not in ('modify_date', 'contents_name'):
            sort = 'modify_date'
    except:
        sort = 'modify_date'
    
    # 정렬
    order = request.args.get('order')
    try:
        order = str.lower(order)
        if order not in ('asc', 'desc'):
            order = 'desc'
    except:
        order = 'desc'

    # 검색
    keyword = request.args.get('keyword')
    if keyword == None:
        keyword = ''
    keyword = '"%' + keyword.strip() + '%"'

    # 페이지당 목록 수
    size = request.args.get('size')
    try:
        size = int(size)
        if size < 0:
            size = 10
    except:
        size = 10

    # 페이지
    page = request.args.get('page')
    try:
        page = int(page)
        if page < 1:
            page = 1
    except:
        page = 1
    page = (page -1) *size

    list = dbHandler.getContents(base_id, keyword, sort, order, size, page)
    jsonStr = json.dumps(list, ensure_ascii=False)

    return jsonStr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)