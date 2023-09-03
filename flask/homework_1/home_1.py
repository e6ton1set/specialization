# Урок 1. Знакомство с Flask
# Задание
#
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/vegetables/')
def vegetables():
    context = {'title': 'Vegetables'}
    return render_template('vegetables.html', **context)


@app.route('/fruits/')
def fruits():
    context = {'title': 'Fruits'}
    return render_template('fruits.html', **context)


if __name__ == '__main__':
    app.run(port=5500)