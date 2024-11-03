from flask import Blueprint, url_for, redirect
from werkzeug.exceptions import HTTPException
lab1 = Blueprint('lab1',__name__)


@lab1.route("/lab1")
def lab():
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
    <a href= "/index">Назад</a>
    <h2>Список роутов</h2>
    <ul class="route-list">
        <li><a href="/index">Индекс</a></li>
        <li><a href="/lab1/web">Web</a></li>
        <li><a href="/lab1/author">Автор</a></li>
        <li><a href="/lab1/oak">Дуб</a></li>
        <li><a href="/lab1/counter">Счетчик</a></li>
        <li><a href="/lab1/reset_counter">Сбросить счетчик</a></li>
        <li><a href="/lab1/info">Информация</a></li>
        <li><a href="/lab1/created">Создано</a></li>
        <li><a href="/lab1/new">Новый</a></li>
        <li><a href="/400">400</a></li>
        <li><a href="/404">404</a></li>
        <li><a href="/401">401</a></li>
        <li><a href="/402">402</a></li>
        <li><a href="/403">403</a></li>
        <li><a href="/405">405</a></li>
        <li><a href="/418">418</a></li>
        <li><a href="/error">Ошибка</a></li>
    </ul>

    </main>

    <footer>
    </footer>
</body>
</html>
'''


@lab1.route("/lab1/web")
def web():
    return """
<!doctype html> 
<html>
<body> 
    <h1>web-сервер на flask</h1> 
    <a href = "/author">author</a>
</body> 
</html>""", 200, {
    'X-Server': 'sample',
    'Content-Type': 'text/plain; charset=utf-8'
}


@lab1.route("/lab1/author")
def author(): 
    name = "Петерс Анна Алексеевна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """
<!doctype html>
<html>
    <body>
        <p>Студент: """ + name + """</p>
        <p>Группа: """ + group + """</p>
        <p>Факультет """ + faculty + """</p>
        <a href = "/web">web</a>
    </body>
</html>"""


@lab1.route('/lab1/oak')
def oak():
    path = url_for("static", filename="lab1/oak.jpg")
    path2 = url_for("static", filename="lab1/lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{path2}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="{path}">
    </body>
<html>
'''

count = 0

@lab1.route('/lab1/counter')
def counter():
    path3 = url_for("static", filename="lab1/lab1.css")
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


@lab1.route('/lab1/reset_counter')
def reset_counter():
    path4 = url_for("static", filename="lab1/lab1.css")
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


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@lab1.route("/lab1/created")
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


@lab1.route("/lab1/new")
def new():
    path9 = url_for("static", filename="lab1/about.jpg")
    return f'''
<!doctype html>
<html>
    <head>
        <title>О себе</title>
        <link rel="stylesheet" type="text/css" href="{url_for("static", filename="lab1.css")}">
    </head>
    <body>
        <header>
            <h1>О себе</h1>
        </header>

        <main>
            <p>Привет! Меня зовут Анна Петерс, и я студентка второго курса 
            направления бизнес-информатика в НГТУ. Это уникальная программа, которая 
            объединяет в себе знания в области экономики, менеджмента и информационных технологий.</p>
            <p>В университете я изучаю широкий спектр дисциплин, от финансового менеджмента и
            маркетинга до программирования и баз данных. Это позволяет мне не только понимать бизнес-процессы, 
            но и применять IT-решения для их оптимизации.</p>
            <p>Я стремлюсь стать профессионалом, способным сочетать глубокое понимание бизнеса
            с техническими навыками. Моя цель — внедрять инновационные IT-решения, 
            которые помогут компаниям повысить эффективность и конкурентоспособность.</p>
            <p>Бизнес-информатика — это не просто сочетание двух слов, это путь к 
            созданию будущего, где технологии и бизнес будут идти рука об руку. 
            Я горжусь тем, что являюсь частью этого направления и готова вносить свой вклад в развитие этой сферы.</p>
            <img src="''' + path9 + '''">

        <footer>
            &copy; Анна Петерс, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
</html>
''', 201, {
    'Content-Language': 'ru; charset="utf-8',
    'X-Server': 'sample',
    'X-Name': 'Peters Anna',
    'X-Group': 'FBI-21',
}