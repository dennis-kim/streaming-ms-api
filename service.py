from flask import Flask, request, jsonify
import dbConnection as db

app = Flask (__name__)

@app.route('/contents/<int:base_id>')
def calling(base_id):
    query = "select contents_name, modify_date from contents c inner join base_dir base ON base.base_dir_id = c.base_dir_id and base.env = 'prd' where base.base_dir_id = %s"
    value = (base_id)
    list = db.selectOneQuery(query, value)
    return 'good!!'

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)