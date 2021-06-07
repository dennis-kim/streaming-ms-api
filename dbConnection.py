import pymysql

def connector():
    conn = pymysql.connect(host='118.34.135.195', port=43306, user='streaming', password='streaming12#', database='STREAMING_DB',charset='utf8')
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