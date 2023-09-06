
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators, DateField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    firstname = StringField('Ваше имя', validators=[DataRequired()])
    lastname = StringField('Ваша фамилия', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password = StringField('Пароль', validators=[DataRequired(), validators.length(min=8)])
    confirm_password = StringField('Повторите пароль',
                                   validators=[DataRequired(), EqualTo('password')]
                                   )
    date_birth = DateField('Дата рождения', format='%Y-%m-%d')