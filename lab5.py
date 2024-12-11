from flask import Blueprint, request, render_template, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)
@lab5.route('/lab5')
def lab():
    username = session.get('login', 'Anonymous') 
    return render_template('lab5/lab5.html', username=username)

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='anna_peters_base',
        user='anna_peters_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory = RealDictCursor)
    return conn, cur
def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not (login and password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    conn, cur = db_connect()
    password_hash = generate_password_hash(password)
    cur.execute(f"SELECT login FROM users WHERE login='{login}';")
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error="Такой пользователь уже существует")
    
    cur.execute (f"INSERT INTO users (login, password) VALUES ('{login}', '{password_hash}');")

    db_close(conn, cur)
    return render_template('lab5/success.html')

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not (login and password):
        return render_template('lab5/login.html', error='Заполните все поля')
    
    conn, cur = db_connect()

    cur.execute(f"SELECT login, password FROM users WHERE login='{login}';")
    user = cur.fetchone()
    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', error="Логин и/или пароль неверны")
    
    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')

    
    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)

