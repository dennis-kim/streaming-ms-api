from flask import Flask
from flask_cors import CORS
import json
import datetime
import dbConnection as db

app = Flask (__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/contents/<int:base_id>')
def calling(base_id):
    query = """
        SELECT 
            contents_name
        FROM 
            contents c 
                INNER JOIN base_dir base 
                        ON base.base_dir_id = c.base_dir_id 
                        AND base.env = 'prd' 
        WHERE 
            base.base_dir_id = %s
    """
    value = (base_id)
    list = db.selectOneQuery(query, value)
    jsonStr = json.dumps(list, ensure_ascii=False)
    #for file in list:
        #convert = json.dumps(file[0])
        #print (convert)
        #return file[0]
    return jsonStr

@app.route('/test')
def test():
    aList = (41, 58, 63)
    jsonStr = json.dumps(aList)
    return jsonStr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)