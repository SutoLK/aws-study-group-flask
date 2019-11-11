"""
AI人生設計勉強会二日目
FlaskによるAPIの作成
    演習問題：オンライン動画の情報を取り扱うAPI
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
programs = []

# 番組の情報をすべて返す
@app.route('/programs')
def all_programs():
    all_data = {'data' : programs}
    return jsonify(all_data)


# 指定された番組の情報を返す
@app.route('/program/<name>')
def search_program(name):
    
    for data in programs:
        if data['title'] == name:
            return jsonify(data)
    
    abort(500, 'Not Found.')


# 指定された番組の情報を追加する
@app.route('/program', methods=['POST'])
def add_program():
    item = request.get_json()
    programs.append(item)
    return jsonify(item)

app.run(host='0.0.0.0', port=80, debug=True)