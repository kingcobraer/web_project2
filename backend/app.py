from flask import Flask, jsonify, request
import sqlite3
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_path():
    # 定义指向Sqlite数据库的路径
    # 注意: windows中复制出来的路径是反斜线\, 不可以直接用!! 必须修改为斜线/ !!!!
    base_dir = 'D:/Files_Nas_PC/IT_Learning/web/projects/AddDelChangeSearch/myproject1/backend/database'    # 数据库文件的路径. 注意: 是斜线/, 而不是反斜线\ !!!! 不管python运行在windows中还是linux中,都是斜线!!
    db_filename = 'student.db'
    db_path = os.path.join(base_dir, db_filename)
    return db_path

def get_all_student_scores():
    db_path =get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    # print(results)
    conn.close()
    return results

def get_customer_search_name(searchTerm):
    db_path =get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name like ?", ('%' + searchTerm + '%',))   ## 注意最后一个逗号!!
    results = cursor.fetchall()
    # print(results)
    conn.close()
    return results

def get_customer_search_multi(col,content):
    print(f"已进入方法:get_customer_search_multi,且获得了参数:col:{col}; content:{content}")
    db_path =get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    #
    # 下面3种方法均可
    #
    # 方法1:
    # sql = f"SELECT * FROM students WHERE {col} like ?"  ## # 构建SQL查询语句，将字段名通过f字符串{}嵌入到SQL字符串中. 注意字段名不可用?进行占位!!! 搜索内容可以用? 进行占位
    # cursor.execute(sql, ('%' + content + '%',))   ## 参数化查询方法. 注意最后一个逗号!! 搜索内容可以用? 进行占位
    # 
    # 方法1变形:
    # cursor.execute(f"SELECT * FROM students WHERE {col} like ?", ('%' + content + '%',))   ## 注意最后一个逗号!! 
    #
    # 方法2:
    sql = f"SELECT * FROM students WHERE {col} like '%{content}%'"
    print(sql)
    cursor.execute(sql)    # 使用字符串拼接构建SQL查询语句，确保输入内容不会引发SQL注入. 更安全的是参数化查询方法.

    #
    results = cursor.fetchall()
    
    conn.close()
    return results

def add_student_score(name, english, math, chinese):
    db_path =get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, english, math, chinese) VALUES (?, ?, ?, ?)",
                   (name, english, math, chinese))
    conn.commit()
    conn.close()

def update_student_score(name, english, math, chinese):
    db_path =get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET english=?, math=?, chinese=? WHERE name=?",
                   (english, math, chinese, name))
    conn.commit()
    conn.close()

def delete_student_score(name):
    db_path =get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()
    conn.close()

@app.route('/api/getStudentScores', methods=['GET'])
def api_get_student_scores():
    results = get_all_student_scores()
    students = []
    for result in results:
        students.append({
            'name': result[1],
            'english': result[2],
            'math': result[3],
            'chinese': result[4]
        })
    return jsonify(students)

@app.route('/api/getStudentScoresSearchName', methods=['GET'])
def api_get_customer_search_name():
    # 获取请求参数
    searchTerm = request.args.get('search','')
    results = get_customer_search_name(searchTerm)
    students = []
    for result in results:
        students.append({
            'name': result[1],
            'english': result[2],
            'math': result[3],
            'chinese': result[4]
        })
    return jsonify(students)

@app.route('/api/getStudentScoresSearchMulti', methods=['GET'])
def api_get_customer_search_multi():
    # 获取请求 多个 搜索参数 !!!
    content = request.args.get('search[content]')    # 注意与单参数相比, 少了一个逗号
    col = request.args.get('search[col]')    # 注意与单参数相比, 少了一个逗号
    if col == '':
        col = 'name'
    print(f"已进入函数:api_get_customer_search_multi, 且获得了参数:col:{col};content:{content}")
    results = get_customer_search_multi(col,content)
    students = []
    for result in results:
        students.append({
            'name': result[1],
            'english': result[2],
            'math': result[3],
            'chinese': result[4]
        })
    return jsonify(students)

@app.route('/api/addStudentScore', methods=['POST'])
def api_add_student_score():
    
    data = request.get_json()
    data = data['_value']      # 组合式API写法,必须加这一句!!  选项式不可加. 原因不知.
    
    #data = request.get_json()['_value']   # 将上面两句合并成一句, 实测可行! 也是标准的简化写法

    # print('这是data数据>>>>>>>>>',data)

    name = data['name']
    english = data['english']
    math = data['math']
    chinese = data['chinese']
    add_student_score(name, english, math, chinese)
    return jsonify({'message': 'Student score added successfully'})

@app.route('/api/updateStudentScore', methods=['PUT'])
def api_update_student_score():
    data = request.get_json()
    name = data['name']
    english = data['english']
    math = data['math']
    chinese = data['chinese']
    update_student_score(name, english, math, chinese)
    return jsonify({'message': 'Student score updated successfully'})

@app.route('/api/deleteStudentScore', methods=['DELETE'])
def api_delete_student_score():
    data = request.get_json()
    name = data['name']
    delete_student_score(name)
    return jsonify({'message': 'Student score deleted successfully'})

if __name__ == '__main__':
    app.run()
