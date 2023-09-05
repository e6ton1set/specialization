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
from models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-data")
def add_data():
    for i in range(1, 6):
        faculty = Faculty(name=f'faculty{i}')
        db.session.add(faculty)

    for i in range(1, 11):
        student = Student(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
            gender=random.choice(['M', 'F']),
            group=random.randint(1, 5),
            id_faculty=random.randint(1, 3)
        )
        db.session.add(student)
    db.session.commit()
    print('DATA ADDED')


@app.route('/')
def index():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)
