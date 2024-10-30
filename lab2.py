from flask import Blueprint, url_for, redirect, render_template, request

lab2 = Blueprint('lab2',__name__)


# 4 задание. Слэш в конце пути
@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'



# 5 задание. Динамические пути
flower_list = [
    {'name': 'роза', 'price': 100},
    {'name': 'тюльпан', 'price': 50},
    {'name': 'незабудка', 'price': 30},
    {'name': 'ромашка', 'price': 20}
]

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        flower = flower_list[flower_id]
        return render_template('flowers.html', flower=flower)

#
@lab2.route('/lab2/all_flowers')
def all_flowers():
    return render_template('all_flowers.html', flowers=flower_list)

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list.clear()
    return render_template('clear_flowers.html')

@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        del flower_list[flower_id]
        return redirect(url_for('lab2.all_flowers'))


# 6 задание. Добавление цветка

@lab2.route('/lab2/add_flower', methods=['GET', 'POST'])
def add_flower():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        flower_list.append({'name': name, 'price': price})
        return redirect(url_for('lab2.all_flowers'))
    else:
        return "Вы не задали имя цветка", 400



# 7 задание. Шаблоны

@lab2.route('/lab2/example')
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

 
@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О сколько нам открытий чудных..."
    return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
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

@lab2.route('/lab2/calc/')
def calc2():
    return redirect(url_for('lab2.calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc3(a):
    return redirect(url_for('lab2.calc', a=a, b=1))



books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Научная фантастика", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 158},
    {"author": "Фрэнсис Скотт Фицджеральд", "title": "Великий Гэтсби", "genre": "Роман", "pages": 180},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480},
    {"author": "Эрих Мария Ремарк", "title": "Три товарища", "genre": "Роман", "pages": 480},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 448},
    {"author": "Виктор Пелевин", "title": "Generation П", "genre": "Сатира", "pages": 320},
    {"author": "Айн Рэнд", "title": "Атлант расправил плечи", "genre": "Философский роман", "pages": 1168},
    {"author": "Стивен Кинг", "title": "Оно", "genre": "Ужасы", "pages": 1138},
]


@lab2.route('/lab2/books')
def list_books():
    return render_template('books.html', books=books)


cars = [
    {"name": "Toyota Camry", "description": "Комфортный седан с отличной топливной экономичностью.", "image": "car1.jpg"},
    {"name": "Ford Mustang", "description": "Мощный спортивный автомобиль с классическим дизайном.", "image": "car2.jpg"},
    {"name": "Tesla Model S", "description": "Электрический седан с передовыми технологиями и высокой производительностью.", "image": "car3.jpg"},
    {"name": "BMW X5", "description": "Роскошный внедорожник с превосходными динамическими характеристиками.", "image": "car4.jpg"},
     {"name": "Mazda CX-5", "description": "Компактный внедорожник с элегантным дизайном и высокой производительностью.", "image": "car5.jpg"},
]


@lab2.route('/lab2/cars')
def list_cars():
    return render_template('cars.html', cars=cars)


@lab2.route('/lab2/')
def labs2():
    return render_template('lab2.html')
