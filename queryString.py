from flask import request

# 장르
def sort():
    sort = request.args.get('sort')
    try:
        sort = str.lower(sort)
        if sort not in ('modify_date', 'contents_name'):
            sort = 'modify_date'
    except:
        sort = 'modify_date'
    return sort

# 정렬
def order():
    order = request.args.get('order')
    try:
        order = str.lower(order)
        if order not in ('asc', 'desc'):
            order = 'desc'
    except:
        order = 'desc'
    return order

# 검색
def keyword():
    keyword = request.args.get('keyword')
    if keyword == None:
        keyword = ''
    keyword = '"%' + keyword.strip() + '%"'
    return keyword

# 페이지당 목록 수
def size():
    size = request.args.get('size')
    try:
        size = int(size)
        if size < 0:
            size = 10
    except:
        size = 10
    return size

# 페이지
def page(size):
    page = request.args.get('page')
    try:
        page = int(page)
        if page < 1:
            page = 1
    except:
        page = 1
    page = (page -1) *size
    return page