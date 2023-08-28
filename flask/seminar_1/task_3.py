# Задание №3
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

from flask import Flask

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


@app.route('/<int:num_1>/<int:num_2/>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


if __name__ == '__main__':
    app.run()

