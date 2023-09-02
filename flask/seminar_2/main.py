# Задания прописаны на странице base.html
from pathlib import PurePath, Path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


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


if __name__ == '__main__':
    app.run()