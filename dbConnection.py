import pymysql
def connector():
    conn = pymysql.connect(host='118.34.135.195', port=43306, user='streaming', password='streaming12#', database='STREAMING_DB',charset='utf8')
    return conn
def selectOneQuery(query, value):
    conn = connector()
    try:
        cursor = conn.cursor()
        cursor.execute(query, value)
        result = cursor.fetchall()
    finally:
        conn.commit()
        conn.close()
    return result