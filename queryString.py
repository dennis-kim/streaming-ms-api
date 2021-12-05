
# 시리즈
def series(series):
    if series is not None:
        try:
            int(series)
            return series
        except:
            return 0
    else:
        return None

# 정렬 타입
def sort(sort):
    try:
        sort = str.lower(sort)
        if sort not in ('modify_date', 'contents_name'):
            sort = 'modify_date'
    except:
        sort = 'modify_date'
    return sort

# 정렬 순서
def order(order):
    try:
        order = str.lower(order)
        if order not in ('asc', 'desc'):
            order = 'desc'
    except:
        order = 'desc'
    return order

# 검색
def keyword(keyword):
    if keyword == None:
        keyword = ''
    keyword = '"%' + keyword.strip() + '%"'
    return keyword

# 페이지당 목록 수
def size(size):
    try:
        size = int(size)
        if size < 1:
            size = 10
    except:
        size = 10
    return size

# 페이지
def page(page, getSize):
    try:
        page = int(page)
        if page < 1:
            page = 1
    except:
        page = 1
    page = (page -1) *getSize
    return page