from flask import Flask, request, jsonify
import dbConnection as db

app = Flask (__name__)

@app.route('/contents/<int:base_id>')
def calling(base_id):
    query = """
        SELECT 
            contents_name
            , modify_date 
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
    return 'good!!'

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)