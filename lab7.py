from flask import Blueprint, render_template, request

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


films = [
    {
        "title": "The Matrix",
        "title_ru": "Матрица",
        "year": 1999,
        "description": "Хакер Нео узнаёт правду о реальности и своей роли в спасении человечества от машин, которые держат мир в иллюзии."
    },
    {
        "title": "Fight Club",
        "title_ru": "Бойцовский клуб",
        "year": 1999,
        "description": "Анонимный герой создаёт подпольный бойцовский клуб, чтобы снять напряжение от своей унылой жизни, но вскоре всё выходит из-под контроля."
    },
    {
        "title": "Gladiator",
        "title_ru": "Гладиатор",
        "year": 2000,
        "description": "Римский генерал Максимус становится гладиатором и жаждет мести императору, который убил его семью и лишил власти."
    }
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        return "Нет фильма под таким индексом", 404

