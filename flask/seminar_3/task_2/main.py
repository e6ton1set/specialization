# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

import random
from flask import Flask, render_template
from models import db, Author, Book, BookAuthor

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app2)


@app2.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app2.cli.command("add-book")
def add_book():
    for i in range(1, 9):
        book = Book(name=f'name{i}',
                    year=i+2000,
                    amount=i
                    )
        db.session.add(book)

    for i in range(1, 15):
        author = Author(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
        )
        db.session.add(author)

    for i in range(1, 15):
        book_author = BookAuthor(
            book_id=random.randint(1, 9),
            author_id=random.randint(1, 14)
        )
        db.session.add(book_author)

    db.session.commit()
    print('DATA ADDED')


@app2.route('/')
def book():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)
