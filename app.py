from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

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
