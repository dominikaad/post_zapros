import sqlite3
from crypt import methods

from flask import Flask, render_template, request, flash
con = sqlite3.connect('bd1.db', check_same_thread=False)
cursor = con.cursor()
app = Flask(__name__)
app.secret_key = '123'

@app.route('/register/')
def page_index():
    return render_template('register.html')

@app.route('/save_register/', methods=['POST', 'GET'])
def save_inf():
    if request.method == 'POST':
        last_name = request.form['last_name']
        name = request.form['name']
        patronymic = request.form['patronymic']
        gender = request.form['gender']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        cursor.execute("INSERT INTO users (last_name, name, patronymic, gender, email, username, password) VALUES (?,?,?,?,?,?,?)",[last_name, name, patronymic, gender, email, username, password])
        con.commit()
    return render_template('1.html')

@app.route('/login/')
def login_user():
    return render_template('login.html')

@app.route('/authorization/',methods=['POST', 'GET'])
def aut_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE username = (?)', [username])
        data = cursor.fetchall()
        if len(data):
            if password == data[-1]:
                flash('Вы авторизованы', 'success')
                return render_template('authorization.html')
            else:
                flash('Неверный логин или пороль', 'danger')
                return render_template('login.html')
    return render_template('authorization.html')


app.run(debug=True)