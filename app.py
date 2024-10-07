from flask import Flask, url_for, redirect, render_template
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
        &copy; Анна Петерс, ФБИ-21, 3 курс, 2024
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

@app.route("/")
@app.route("/lab1/web")
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

@app.route("/lab1/author")
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
        <img src="{path}">
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


@app.route("/lab1/new")
def new():
    path9 = url_for("static", filename="about.jpg")
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

## Лабораторная работа 2

# 4 задание. Слэш в конце пути
@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'



# 5 задание. Динамические пути
flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
          flower = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Цветок</h1>
    <p>Цветок: {flower}</p>
    <a href="/lab2/all_flowers">Посмотреть все цветы</a>
    </body>
</html>
'''

#
@app.route('/lab2/all_flowers')
def all_flowers():
    flowers_html = ''
    for flower in flower_list:
        flowers_html += f'<li>{flower}</li>'
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Все цветы</h1>
    <p>Всего цветов: {len(flower_list)}</p>
    <ul>
        {flowers_html}
    </ul>
     <a href="/lab2/clear_flowers">Очистить цветы</a>
    </body>
</html>
'''
@app.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list.clear()
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список цветов очищен</h1>
    <p>Все цветы удалены</p>
    <a href="/lab2/all_flowers">Посмотреть все цветы</a>
    </body>
</html>
'''




# 6 задание. Добавление цветка

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
<html>
'''

@app.route('/lab2/add_flower/')
def add_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Ошибка</h1>
    <p>Вы не задали имя цветка</p>
    </body>
</html>
''', 400


# 7 задание. Шаблоны

@app.route('/lab2/example')
def example():
   name, numberlab, group, course = 'Анна Петерс', 2, 'ФБИ-21', 3
   fruits = [
       {'name': 'яблоки', 'price': 100},
       {'name': 'груши','price': 120},
       {'name': 'апельсины', 'price': 80},
       {'name': 'мандарины', 'price': 95},
       {'name': 'манго', 'price': 321 }
   ] 
   return render_template('example.html',
                          name=name, group=group, numberlab=numberlab, course=course, fruits=fruits)

 
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О сколько нам открытий чудных..."
    return render_template('filter.html', phrase = phrase)


@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    Сумма = a + b
    Вычитание = a - b
    Умножение = a * b
    Деление = a / b if b != 0 else "Деление на ноль!!"
    Степень = a ** b

    return f"""
    <h1>Калькулятор</h1>
    Сумма: {a} + {b} = {Сумма}<br>
    Вычитание: {a} - {b} = {Вычитание}<br>
    Умножение: {a} × {b} = {Умножение}<br>
    Деление: {a} / {b} = {Деление}<br>
    Cтепень: {a} <sup>{b}</sup> = {Степень}<br>
    """

@app.route('/lab2/calc/')
def calc2():
    return redirect(url_for('calc', a=1, b=1))


@app.route('/lab2/calc/<int:a>')
def calc3(a):
    return redirect(url_for('calc', a=a, b=1))



