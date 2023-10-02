# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def print_hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route('/string/<string:text>/')
def get_len_str(text: str) -> str:
    return str(len(text))


@app.route('/students/')
def students():
    head = {
        'firstname': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл',
    }

    students_list = [
        {
            'firstname': 'Николай',
            'lastname': 'Иванов',
            'age': 20,
            'rating': 4.6,
        },
        {
            'firstname': 'Оксана',
            'lastname': 'Маркина',
            'age': 19,
            'rating': 4.5,
        },
        {
            'firstname': 'Хасан',
            'lastname': 'Пургель',
            'age': 20,
            'rating': 4.1
        }
    ]

    return render_template('my_temp.html', **head, students_list=students_list)


@app.route('/index/')
def index():
    return render_template('my_temp.html')


if __name__ == '__main__':
    app.run()
