# Задание №3
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from forms import RegisterForm
from models import db, User

app3 = Flask(__name__)
app3.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app3)
app3.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app3)


@app3.cli.command("init-user")
def init_user():
    db.create_all()
    print('OK')


@app3.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))

    return render_template('register.html', form=form)


@app3.route('/users/')
def users():
    all_users = User.query.all()
    context = {'users': all_users}
    return render_template('users.html', **context)
