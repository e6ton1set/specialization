# Задание №4
# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.


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


@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route('/string/<string:text>/')
def get_len_str(text: str) -> str:
    return str(len(text))


if __name__ == '__main__':
    app.run()