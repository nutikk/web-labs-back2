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
    
@lab7.route('/lab7/rest-api/films/', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204
    else:
        return "Нет фильма под таким индексом", 404
    
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json()
        films[id] = film
        return films[id]
    else:
        return "Нет фильма под таким индексом", 404
    
@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    new_film = request.get_json()

    required_fields = ["title", "title_ru", "year", "description"]
    if not all(field in new_film for field in required_fields):
        return {"error": "Missing required fields"}, 400

    films.append(new_film)

    new_index = len(films) - 1
    return {"id": new_index}, 201
    


