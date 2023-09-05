from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'{self.name}'
