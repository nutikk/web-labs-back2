from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    age = request.cookies.get('age')
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name','Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color','magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    if user == '':
        errors['user'] = 'Заполните поле!'
    elif age == '':
        errors['age']  = 'Заполнитe поле!'
   
    return render_template('lab3/form1.html', user=user, sex=sex, age=age, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price=0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('/lab3/pay.html', price=price) 


@lab3.route('/lab3/success', methods=['get','post'])
def success():
    if request.method == 'POST':
        price = request.form.get('price')
    else:
        price = request.args.get('price') 
    return render_template('/lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background_color = request.args.get('background_color')
    font_size = request.args.get('font_size')
    padding = request.args.get('padding')
    
    if color or background_color or font_size:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if padding:
            resp.set_cookie('padding', padding)
        return resp
    
    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')
    
    resp = make_response(render_template('lab3/settings.html', color=color, 
                                         background_color=background_color,
                                          font_size=font_size,padding=padding))
    return resp



@lab3.route('/lab3/ticket', methods=['get', 'post'])
def ticket():
    errors = {}
    if request.method == 'POST':
        fio = request.form.get('fio')
        berth = request.form.get('berth')
        with_linen = request.form.get('with_linen')
        with_baggage = request.form.get('with_baggage')
        age = request.form.get('age')
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        travel_date = request.form.get('travel_date')
        with_insurance = request.form.get('with_insurance')

        if not fio:
            errors['fio'] = 'Заполните поле ФИО!'
        if not berth:
            errors['berth'] = 'Выберите место!'
        if not age:
            errors['age'] = 'Заполните поле возраста!'
        if not departure:
            errors['departure'] = 'Заполните поле пункта выезда!'
        if not destination:
            errors['destination'] = 'Заполните поле пункта назначения!'
        if not travel_date:
            errors['travel_date'] = 'Заполните поле даты поездки!'

        if age:
            age = int(age)
            if not (1 <= age <= 120):
                errors['age'] = 'Возраст должен быть от 1 до 120 лет!'
        else:
            errors['age'] = 'Заполните поле возраста!'

        if errors:
            return render_template('lab3/ticket_form.html', errors=errors, fio=fio, berth=berth, with_linen=with_linen, with_baggage=with_baggage, age=age, departure=departure, destination=destination, travel_date=travel_date, with_insurance=with_insurance)

        price = 700 if age < 18 else 1000
        if berth in ['нижняя', 'нижняя боковая']:
            price += 100
        if with_linen:
            price += 75
        if with_baggage:
            price += 250
        if with_insurance:
            price += 150

        ticket = {
            'fio': fio,
            'berth': berth,
            'with_linen': 'Да' if with_linen else 'Нет',
            'with_baggage': 'Да' if with_baggage else 'Нет',
            'age': age,
            'departure': departure,
            'destination': destination,
            'travel_date': travel_date,
            'with_insurance': 'Да' if with_insurance else 'Нет',
            'price': price,
            'is_child': age < 18
        }

        return render_template('lab3/ticket.html', ticket=ticket)

    return render_template('lab3/ticket_form.html', errors=errors)