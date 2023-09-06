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
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        key = Fernet.generate_key()
        fernet = Fernet(key)
        enctex = fernet.encrypt(password.encode())
        date_birth = form.date_birth.data.strftime('%Y-%m-%d')
        user = User(firstname=firstname,
                    lastname=lastname,
                    email=email,
                    password=enctex,
                    date_birth=date_birth
                    )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))

    return render_template('registration.html', form=form)


@app.route('/users/')
def users():
    all_users = User.query.all()
    context = {'users': all_users}
    return render_template('users.html', **context)
