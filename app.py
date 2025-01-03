from flask import Flask, url_for
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

from dotenv import load_dotenv
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3 
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from rgz import rgz
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

app.config['DB_TYPE'] = 'postgres'

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'anna_peters_orm'
    db_user = 'anna_peters_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anna_peters_orm:123@127.0.0.1:5432/anna_peters_orm'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "anna_peters_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'


db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(rgz)


class PaymentRequired(HTTPException):
    code = 402
    description = 'Требуется оплата'

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

@app.route("/index")
def index():
    path5 = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href="{path5}">
    <body>
    <head>
        <header>
        <h1>НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных»<h1>
        </header>

        <main>
        <a href= "/lab1">Первая лабораторная работа</a><br>
        <a href= "/lab2/">Вторая лабораторная работа</a><br>
        <a href ="/lab3/">Третья лабораторная работа</a><br>
        <a href ="/lab4/">Четвертая лабораторная работа</a><br>
        <a href ="/lab5">Пятая лабораторная работа</a><br>
        <a href ="/lab6/">Шестая лабораторная работа</a><br>
        <a href ="/lab7/">Седьмая лабораторная работа</a><br>
        <a href ="/lab8/">Восьмая лабораторная работа</a><br>
        <a href ="/lab9/">Девятая лабораторная работа</a><br>
        <a href ="/rgz">РГЗ</a>

        </main>

        <footer>
        &copy; Анна Петерс, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.route("/400")
def error_400():
    return '''
<!doctype html>
<html>
<head>
    <title>400 Плохой запрос</title>
</head>
<body>
    <h1>400 Плохой запрос</h1>
    <p>Сервер не смог понять запрос из-за неверного синтаксиса.</p>
    <p>Код ошибки: 400</p>
</body>
</html>
    ''', 400

@app.route("/401")
def error_401():
    return '''
<!doctype html>
<html>
<head>
    <title>401 Неавторизованный</title>
</head>
<body>
    <h1>401 Неавторизованный</h1>
    <p>Запрос требует аутентификации пользователя.</p>
    <p>Код ошибки: 401</p>
</body>
</html>
    ''', 401

@app.route("/402")
def error_402():
    return '''
<!doctype html>
<html>
<head>
    <title>402 Требуется оплата</title>
</head>
<body>
    <h1>402 Требуется оплата</h1>
    <p>Этот код зарезервирован для будущего использования.</p>
    <p>Код ошибки: 402</p>
</body>
</html>
    ''', 402

@app.route("/403")
def error_403():
    return '''
<!doctype html>
<html>
<head>
    <title>403 Запрещено</title>
</head>
<body>
    <h1>403 Запрещено</h1>
    <p>Сервер понял запрос, но отказывается его выполнять.</p>
    <p>Код ошибки: 403</p>
</body>
</html>
    ''', 403

@app.route("/405")
def error_405():
    return '''
<!doctype html>
<html>
<head>
    <title>405 Метод не разрешен</title>
</head>
<body>
    <h1>405 Метод не разрешен</h1>
    <p>Указанный в запросе метод не разрешен для ресурса, идентифицированного URI.</p>
    <p>Код ошибки: 405</p>
</body>
</html>
    ''', 405

@app.route("/418")
def error_418():
    return '''
<!doctype html>
<html>
<head>
    <title>418 Я — чайник</title>
</head>
<body>
    <h1>418 Я — чайник:)</h1>
    <p>Сервер отказывается варить кофе, потому что он, навсегда, чайник.</p>
    <p>Код ошибки: 418</p>
</body>
</html>
    ''', 418

@app.errorhandler(404)
def not_found(err):
    path7 = url_for("static", filename="lab1.css")
    path8 = url_for("static", filename="orig.jpg")
    return f'''
<!doctype html>
<html>
<head>
    <title>404 Не найдено</title>
    <link rel="stylesheet" type="text/css" href="{path7}">
</head>
<body>
    <main>
        <h1>404 Не найдено</h1>
        <p>Подумайте ещё раз, мой друг. Такой страницы не существует!</p>
        <p>Код ошибки: 404</p>
    <div class = img1>
        <img src="''' + path8 + '''">
    <div>
    </main>
</body>
</html>
    ''', 404

@app.route("/error")
def trigger_error():
    # деление на ноль
    return 1 / 0, 500

@app.errorhandler(500)
def error_500(err):
    return '''
<!doctype html>
<html>
<head>
    <title>500 Внутренняя ошибка сервера</title>
</head>
<body>
    <h1>500 Внутренняя ошибка сервера</h1>
    <p>Произошла ошибка на сервере. Пожалуйста, попробуйте позже.</p>
    <p>Код ошибки: 500</p>
</body>
</html>
    ''', 500
