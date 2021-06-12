import pymysql

def connector():
    conn = pymysql.connect(host='msnas.i234.me', port=43306, user='streaming', password='streaming12#', database='STREAMING_DB',charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    return conn

def selectQuery(query):
    conn = connector()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    finally:
        conn.commit()
        conn.close()
    return result