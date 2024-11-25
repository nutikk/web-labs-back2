from flask import Blueprint, render_template, request, redirect, session 
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error = 'Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error = 'На ноль делить нельзя')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '':
        x1 = 0
    else:
        x1 = int(x1)
    
    if x2 == '':
        x2 = 0
    else:
        x2 = int(x2)
    
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '':
        x1 = 1
    else:
        x1 = int(x1)
    
    if x2 == '':
        x2 = 1
    else:
        x2 = int(x2)
    
    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error = 'Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/exp-form')
def exp_form():
    return render_template('lab4/exp-form.html')

@lab4.route('/lab4/exp', methods=['POST'])
def exp():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/exp.html', error = 'Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0:
        return render_template('lab4/exp.html', error = 'Число не должно быть равно 0!')
    if x2 == 0:
        return render_template('lab4/exp.html', error = 'Число не должно быть равно 0!')#Ну если честно,возведение любого числа в степень "0" равно 1
    #Вроде это не считается ошибкой
    result = x1 ** x2
    return render_template('lab4/exp.html', x1=x1, x2=x2, result=result)

tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count, max_tree=10)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 10:
            tree_count += 1
    
    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Smith', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Johnson', 'gender': 'male'},
    {'login': 'anya', 'password': '777', 'name': 'Anya Peters', 'gender': 'female'},
    {'login': 'john', 'password': '888', 'name': 'John Doe', 'gender': 'male'}
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        authorized = 'login' in session
        login = session.get('login', '')
        user = next((user for user in users if user['login'] == login), None)
        name = user['name'] if user else ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        return render_template('lab4/login.html', error='не введён логин', authorized=False, login='', password='')

    if not password:
        return render_template('lab4/login.html', error='не введён пароль', authorized=False, login=login, password='')

    user = next((user for user in users if user['login'] == login and user['password'] == password), None)
    if user:
        session['login'] = login
        return redirect('/lab4/login')

    return render_template('lab4/login.html', error='неверные логин и/или пароль', authorized=False, login='', password='')

@lab4.route('/lab4/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


