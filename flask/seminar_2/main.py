# Задания прописаны на странице login.html

from pathlib import PurePath, Path
from venv import logger
from flask import Flask, render_template, request, abort, redirect, url_for, flash
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def base():
    return render_template('login.html')


@app.route('/next/')
def next_page():
    return f'Привет, Вася!'


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    contex = {'title': 'Задание 2'}
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {escape(file_name)} загружен на сервер"
    return render_template('upload.html', **contex)


@app.route('/authentication/', methods=['GET', 'POST'])
def authentication():
    users = {
        'auth_email': '1@mail.ru',
        'auth_pass': '123'
    }
    contex = {'title': 'Задание 3'}
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if auth_email == users.get('auth_email') and auth_pass == users['auth_pass']:
            return f'Вход с почты {escape(auth_email)} выполнен успешно.'
        else:
            return 'Ошибка входа'
    return render_template('authentication.html', **contex)


@app.route('/message/', methods=['GET', 'POST'])
def message():
    contex = {'title': 'Задание 4'}
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Ваш текст: "{escape(text)}"<br><br>Количество слов: {len(text.split())}'
    return render_template('message.html', **contex)


@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    contex = {'title': 'Задание 5'}
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')

        match operation:
            case 'add':
                result = int(num1) + int(num2)
                return f'Результат выражения {num1} {operation} {num2} равен {result}'
            case 'subtract':
                result = int(num1) - int(num2)
                return f'Результат выражения {num1} {operation} {num2} равен {result}'
            case 'multiply':
                result = int(num1) * int(num2)
                return f'Результат выражения {num1} {operation} {num2} равен {result}'
            case 'divide':
                if num2 == '0':
                    return f'{float("inf")}'
                result = int(num1) / int(num2)
                return f'Результат выражения {num1} {operation} {num2} равен {result}'
    return render_template('calc.html', **contex)


@app.errorhandler(403)
def error403(e):
    logger.warning(e)
    context = {
        'title': 'Доступ запрещён',
        'url': request.base_url,
    }
    return render_template('error403.html', **context), 403


@app.route('/validate_age/', methods=['GET', 'POST'])
def validate_age():
    MIN_AGE = 18
    MAX_AGE = 110
    contex = {'title': 'Задание 6'}
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if MIN_AGE <= int(age) <= MAX_AGE:
            return f'{name}, добро пожаловать!'
        else:
            abort(403)
    return render_template('validate_age.html', **contex)


@app.route('/quadro/', methods=['GET', 'POST'])
def quadro():
    num = 5
    return redirect(url_for('quadro_res', num=int(num**2)))


@app.route('/quadro/<int:num>')
def quadro_res(num: int):
    return str(num)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))

    contex = {'title': 'Задание 8'}
    return render_template('form.html', **contex)


if __name__ == '__main__':
    app.run()
