from flask import Flask, url_for, redirect
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

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
        <a href= "/lab1">Первая лабораторная работа</a>
        </main>

        <footer>
        &copy; Анна Петерс, ФБИ-21, 2 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    path6 = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
<head>
    <title>Лабораторная работа 1</title>
    <link rel="stylesheet" type="text/css" href="{path6}">
</head>
<body>
    <header>
    </header>

    <main>
    <div class=flask>
    Flask — фреймворк для создания веб-приложений на языке
    программирования Python, использующий набор инструментов
    Werkzeug, а также шаблонизатор Jinja2.
    <br>Относится к категории так называемых
    микрофреймворков — минималистичных каркасов
    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
    </div>
    <a href= "/index"><Назад</a>
    </main>

    <footer>
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



@app.route("/")
@app.route("/lab1/web")
def web():
    return """<!doctype html> 
        <html>
           <body> 
               <h1>web-сервер на flask</h1> 
           </body> 
           <a href = "/author">author</a>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author(): 
    name = "Петерс Анна Алексеевна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет """ + faculty + """</p>
                <a href = "/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    path2 = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{path2}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
<html>
'''

count = 0

@app.route('/lab1/counter')
def counter():
    path3 = url_for("static", filename="lab1.css")
    global count
    count += 1
    return f'''
<!doctype html>
<html>
<head>
        <link rel="stylesheet" type="text/css" href="{path3}">
    </head>
    <body>
        <div>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        </div>
        <div class ="button">
        <a href= "/lab1/reset_counter">Отчистить счётчик</a>
        </div>
    </body>
</html>
'''

@app.route('/lab1/reset_counter')
def reset_counter():
    path4 = url_for("static", filename="lab1.css")
    global count
    count = 0
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{path4}">
    </head>
    <body>
        <div>
            Количество заходов на страницу: ''' + str(count) + '''
        </div>
        <div class="button">
            <a href= "/lab1/counter">Посчитать количество заходов</a>
        </div>
         <div>
            <h2>Счетчик отчищен!</h2>
        </div>
    </body>
</html>
'''


@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

