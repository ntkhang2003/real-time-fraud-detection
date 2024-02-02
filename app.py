from flask import Flask, render_template
import pymysql
import time

app = Flask(__name__)

# Cấu hình kết nối MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'khang',
    'database': 'creditcard',
}

@app.route('/')
def index():
    # Kết nối đến MySQL
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    return render_template('index.html')

@app.route('/demo1')
def demo1():
    # Kết nối đến MySQL
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    # Thực hiện truy vấn
    try:
        cursor.execute("SELECT * FROM new_transaction")
        data = cursor.fetchall()
    except:
        data = []
        pass
    # Xuất ra trang HTML
    return render_template('demo1.html', data=data)

@app.route('/demo2')
def demo2():
    # Kết nối đến MySQL
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    # Thực hiện truy vấn
    try:
        cursor.execute("SELECT * FROM new_transaction")
        data = cursor.fetchall()
    except:
        data = []
        pass
    # Xuất ra trang HTML
    return render_template('demo2.html', data=data)

@app.route('/customer/<cc_num>')
def show_cust(cc_num):
    # Kết nối đến MySQL
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM customer WHERE customer.cc_num = {cc_num}")
    data = cursor.fetchall()
    return render_template('cust.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)