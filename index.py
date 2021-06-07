from flask import Flask, request
from flask_cors import CORS
import json
import dbHandler

app = Flask (__name__)
CORS(app)
 
@app.route('/contents/<int:base_id>')
def getContents(base_id):
    sort = request.args['sort']
    order = request.args['order']

    list = dbHandler.getContents(base_id, sort, order)
    jsonStr = json.dumps(list, ensure_ascii=False)

    return jsonStr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)